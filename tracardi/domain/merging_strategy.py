
NESTED_DICT = 'nested_dict'

# String, Int
LATEST_UPDATE = 'latest_update'
EARLIEST_UPDATE = 'earliest_update'

# Dates
LATEST_DATE = 'latest_date'
EARLIEST_DATE = 'earliest_date'

# Bool
ALWAYS_TRUE = 'always_true'
ALWAYS_FALSE = 'always_false'
AND = 'and'
OR = 'or'

# Integer
ADD = 'add'
MAX = 'max'
MIN = 'min'

# List
UNIQUE_EXTEND = 'unique_extend'
EXTEND = 'extend'


allowed_merges_by_type = {
    'str': [LATEST_UPDATE, EARLIEST_UPDATE]
}