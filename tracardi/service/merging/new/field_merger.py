from collections import namedtuple

from typing import List

from pydantic import BaseModel

from tracardi.service.merging.new.field_ref import FieldRef
from tracardi.service.merging.new.merging_strategy_types import id_to_strategy, StrategyRecord
from tracardi.service.merging.new.strategy_protocol import StrategyProtocol

MergedValue = namedtuple('MergedValue', ['value', 'timestamp', 'strategy_id'])


class FieldMerger(BaseModel):
    field: str
    values: List[FieldRef]
    type: str
    strategies: List[str] = []

    @staticmethod
    def _invoke_strategy(strategy: StrategyProtocol) -> FieldRef:
        if not strategy.prerequisites():
            raise AssertionError("Strategy prerequisites not met.")
        return strategy.merge()

    def merge(self) -> MergedValue:
        for strategy_id in self.strategies:
            strategy: StrategyRecord = id_to_strategy.get(strategy_id, None)
            if not strategy:
                raise ValueError(f"Unknown merging strategy '{strategy_id}'.")
            try:
                result = self._invoke_strategy(strategy.strategy(self))
                return MergedValue(result.value, result.timestamp, strategy_id)
            except AssertionError:
                continue
        raise ValueError("Could not merge, No merging strategy qualified for value merging.")

