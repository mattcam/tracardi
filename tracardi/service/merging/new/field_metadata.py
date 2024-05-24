from collections import namedtuple

from dotty_dict import Dotty
from typing import List, Optional

from pydantic import BaseModel

from tracardi.service.merging.new.merging_strategy_types import id_to_strategy, StrategyRecord
from tracardi.service.merging.new.strategy_protocol import StrategyProtocol
from tracardi.service.merging.new.value_timestamp import ValueTimestamp

MergedValue = namedtuple('MergedValue', ['value', 'timestamp', 'strategy_id'])


class FieldMetaData(BaseModel):
    path: Optional[str] = None
    field: str
    values: List[ValueTimestamp]
    type: str
    strategies: List[str] = []

    @staticmethod
    def _invoke_strategy(strategy: StrategyProtocol) -> ValueTimestamp:
        if not strategy.prerequisites():
            raise AssertionError("Strategy prerequisites not met.")
        return strategy.merge()

    def merge(self, profile: Dotty) -> MergedValue:
        for strategy_id in self.strategies:
            strategy: StrategyRecord = id_to_strategy.get(strategy_id, None)
            if not strategy:
                raise ValueError(f"Unknown merging strategy '{strategy_id}'.")
            try:
                print(strategy.strategy)
                result = self._invoke_strategy(strategy.strategy(profile, self))
                return MergedValue(result.value, result.timestamp, strategy_id)
            except AssertionError:
                continue
        raise ValueError("Could not merge, No merging strategy qualified for value merging.")


    def field_values(self):
        return [value.value for value in self.values]
