from collections import namedtuple

from typing import List, Any, Tuple, Optional, Union, Callable

from datetime import datetime

from pydantic import BaseModel

from tracardi.service.merging.new.merging_strategy_types import id_to_strategy
from tracardi.service.merging.new.strategy_protocol import StrategyProtocol

MergedValue = namedtuple('MergedValue', ['value', 'timestamp', 'strategy_id'])


class FieldMerger(BaseModel):
    field: str
    values: List[Tuple[Any, Union[Optional[datetime], Optional[float]]]]
    type: str
    strategies: List[str] = []

    @staticmethod
    def _invoke_strategy(strategy: StrategyProtocol):
        if not strategy.prerequisites():
            raise AssertionError("Strategy prerequisites not met.")
        return strategy.merge()

    def merge(self) -> MergedValue:
        for strategy_id in self.strategies:
            strategy: Callable = id_to_strategy.get(strategy_id, None)
            if not strategy:
                raise ValueError(f"Unknown merging strategy '{strategy_id}'.")
            try:
                result = self._invoke_strategy(strategy(self))
                return MergedValue(result[0], result[1], strategy_id)
            except AssertionError:
                continue
        raise ValueError("Could not merge, No merging strategy qualified for value merging.")

