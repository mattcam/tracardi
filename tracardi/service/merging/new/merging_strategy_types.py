from typing import Callable

from tracardi.domain.named_entity import NamedEntity
from tracardi.service.merging.new.strategy.bool_strategy import AlwaysTrueStrategy, AlwaysFalseStrategy, AndStrategy, \
    OrStrategy
from tracardi.service.merging.new.strategy.datetime_strategy import MinDateTimeStrategy, MaxDateTimeStrategy
from tracardi.service.merging.new.strategy.list_strategy import ConCatStrategy, ConCatDistinctStrategy
from tracardi.service.merging.new.strategy.value_strategy import MinValueStrategy, SumValueStrategy, MaxValueStrategy, \
    AvgValueStrategy
from tracardi.service.merging.new.strategy.value_update_strategy import LastUpdateStrategy, FirstUpdateStrategy


class StrategyRecord(NamedEntity):
    description: str
    strategy: Callable


NESTED_DICT = 'nested_dict'

# Value Updates
LAST_UPDATE = 'last_update'
FIRST_UPDATE = 'first_update'

# Value Updates
LAST_DATETIME = 'last_datetime'
FIRST_DATETIME = 'first_datetime'

# Bool
ALWAYS_TRUE = 'always_true'
ALWAYS_FALSE = 'always_false'
AND = 'and'
OR = 'or'

# Integer
SUM = 'sum'
AVG = 'avg'
MAX = 'max'
MIN = 'min'

# List
UNIQUE_CONCAT = 'unique_concat'
CONCAT = 'concat'
FIRST = 'first'
LAST = 'last'

allowed_merges_by_type = {
    'str': [LAST_UPDATE, FIRST_UPDATE]
}

id_to_strategy = {

    LAST_UPDATE: StrategyRecord(
        id=LAST_UPDATE,
        name="Last updated value",
        description="This merge strategy use update date to find the most fresh that will prevail.",
        strategy=LastUpdateStrategy),
    FIRST_UPDATE: StrategyRecord(
        id=LAST_UPDATE,
        name="First inserted value",
        description="This merge strategy use update date to find the first inserted that will prevail",
        strategy=FirstUpdateStrategy),

    MIN: StrategyRecord(
        id=MIN,
        name="Minimal value",
        description="This merge strategy will select minimal value as merged value",
        strategy=MinValueStrategy
    ),
    MAX: StrategyRecord(
        id=MAX,
        name="Maximal value",
        description="This merge strategy will select maximal value as merged value",
        strategy=MaxValueStrategy),
    SUM: StrategyRecord(
        id=SUM,
        name="Sum of values",
        description="This merge strategy will sum all values and return it as merged value",
        strategy=SumValueStrategy),
    AVG: StrategyRecord(
        id=AVG,
        name="Average of values",
        description="This merge strategy will average all values and return it as merged value",
        strategy=AvgValueStrategy),

    LAST_DATETIME: StrategyRecord(
        id=LAST_DATETIME,
        name="Last date",
        description="This merge strategy works only on date values and it will select last date as merged value",
        strategy=MaxDateTimeStrategy),
    FIRST_DATETIME: StrategyRecord(
        id=FIRST_DATETIME,
        name="First date",
        description="This merge strategy works only on date values and it will select first date as merged value",
        strategy=MinDateTimeStrategy),

    ALWAYS_TRUE: StrategyRecord(
        id=ALWAYS_TRUE,
        name="Always TRUE",
        description="This merge strategy always True as merged value",
        strategy=AlwaysTrueStrategy),
    ALWAYS_FALSE: StrategyRecord(
        id=ALWAYS_FALSE,
        name="Always FALSE",
        description="This merge strategy always False as merged value",
        strategy=AlwaysFalseStrategy),
    AND: StrategyRecord(
        id=AND,
        name="AND Operator",
        description="This merge strategy will use AND operator on all boolean values and will return it as merged value",
        strategy=AndStrategy),
    OR: StrategyRecord(
        id=OR,
        name="OR Operator",
        description="This merge strategy will use OR operator on all boolean values and will return it as merged value",
        strategy=OrStrategy),

    CONCAT: StrategyRecord(
        id=ALWAYS_FALSE,
        name="Concatenate Values",
        description="This merge strategy is used on lists and will concatenate all values and return it as merged value",
        strategy=ConCatStrategy),
    UNIQUE_CONCAT: StrategyRecord(
        id=ALWAYS_FALSE,
        name="Concatenate Unique Values",
        description="This merge strategy is used on lists and will concatenate all values and return unique values it as merged value",
        strategy=ConCatDistinctStrategy)
}
