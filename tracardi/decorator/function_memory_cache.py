import asyncio
from typing import Dict, Tuple, Any

import functools

from tracardi.event_server.utils.memory_cache import MemoryCache, CacheItem

cache: Dict[str, MemoryCache] = {}

def _run_function(func, args, kwargs, max_size, allow_null_values) -> Tuple[Any, str, str]:
    # Construct a unique cache key from the function's module name,
    # function name, args, and kwargs to avoid collisions.

    key_parts = [func.__module__, func.__qualname__, ]
    func_key = ':'.join(map(str, key_parts))

    key_parts = [args]
    key_parts.extend(f'{k}={v}' for k, v in kwargs.items())
    args_key = ':'.join(map(str, key_parts))

    # Create cache
    if func_key not in cache:
        cache[func_key] = MemoryCache(func_key, max_pool=max_size, allow_null_values=allow_null_values)

    # Check cache
    if args_key in cache[func_key]:
        return cache[func_key][args_key].data, func_key, args_key

    result = func(*args, **kwargs)

    return result, func_key, args_key

def async_cache_for(ttl, max_size=1000, allow_null_values=False):
    def decorator(func):
        @functools.wraps(func)
        async def async_wrapper(*args, **kwargs):

            result, func_key, args_key = _run_function(func, args, kwargs, max_size, allow_null_values)
            if asyncio.iscoroutine(result):
                result = await result

            # Update cache
            cache[func_key][args_key] = CacheItem(data=result, ttl=ttl)
            return result

        return async_wrapper

    return decorator


def cache_for(ttl, max_size=1000, allow_null_values=False):
    def decorator(func):

        @functools.wraps(func)
        def sync_wrapper(*args, **kwargs):
            result, func_key, args_key = _run_function(func, args, kwargs, max_size, allow_null_values)

            # Update cache
            cache[func_key][args_key] = CacheItem(data=result, ttl=ttl)
            return result

        return sync_wrapper

    return decorator
