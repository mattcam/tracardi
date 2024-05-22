from tracardi.service.merging.new.strategy.bool_strategy import AlwaysTrueStrategy, AlwaysFalseStrategy, AndStrategy, \
    OrStrategy
from tracardi.service.merging.new.strategy.datetime_strategy import MinDateTimeStrategy, MaxDateTimeStrategy
from tracardi.service.merging.new.strategy.list_strategy import ConCatStrategy, ConCatDistinctStrategy
from tracardi.service.merging.new.strategy.value_strategy import MinValueStrategy, SumValueStrategy, MaxValueStrategy, \
    AvgValueStrategy
from tracardi.service.merging.new.strategy.value_update_strategy import LastUpdateStrategy, FirstUpdateStrategy

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


allowed_merges_by_type = {
    'str': [LAST_UPDATE, FIRST_UPDATE]
}

id_to_strategy = {
    LAST_UPDATE: LastUpdateStrategy,
    FIRST_UPDATE: FirstUpdateStrategy,

    MIN: MinValueStrategy,
    MAX: MaxValueStrategy,
    SUM: SumValueStrategy,
    AVG:AvgValueStrategy,

    LAST_DATETIME: MaxDateTimeStrategy,
    FIRST_DATETIME: MinDateTimeStrategy,

    ALWAYS_TRUE: AlwaysTrueStrategy,
    ALWAYS_FALSE: AlwaysFalseStrategy,
    AND: AndStrategy,
    OR: OrStrategy,

    CONCAT: ConCatStrategy,
    UNIQUE_CONCAT: ConCatDistinctStrategy
}