from typing import Protocol, List, Tuple, Any, Union, Optional
from datetime import datetime


class StrategyProtocol(Protocol):
    def prerequisites(self) -> bool:
        ...

    def merge(self) -> Tuple[Any, Union[Optional[datetime], Optional[float]]]:
        ...