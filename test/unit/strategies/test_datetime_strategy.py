from dotty_dict import Dotty

from tracardi.service.merging.new.field_metadata import FieldMetaData
from tracardi.service.merging.new.merging_strategy_types import FIRST_DATETIME, LAST_DATETIME
from tracardi.service.merging.new.strategy.datetime_strategy import MinDateTimeStrategy, MaxDateTimeStrategy
from tracardi.service.merging.new.value_timestamp import ValueTimestamp


def test_first_datetime_strategy():
    first = ValueTimestamp(value='2004-01-18T17:13:28.620880Z')
    second =  ValueTimestamp(value= '2024-05-18T17:13:28.620880+00:00')
    third =  ValueTimestamp(value='2024-05-18T17:13:28.620880+00:00')

    field = FieldMetaData(
        field="x",
        values=[second, first],
        type="datetime",
        strategies=[FIRST_DATETIME]
    )

    mvs = MinDateTimeStrategy(Dotty({}), field)
    assert mvs.prerequisites()
    assert mvs.merge().value.year == 2004

    first = ValueTimestamp(value={})
    second = ValueTimestamp(value='2023-01-01')

    field = FieldMetaData(
        field="x",
        values=[third, second, first],
        type="datetime",
        strategies=[FIRST_DATETIME]
    )
    mvs = MinDateTimeStrategy(Dotty({}), field)
    assert not mvs.prerequisites()



def test_last_datetime_strategy():
    first =  ValueTimestamp(value='2002-01-01')
    second =  ValueTimestamp(value='2023-01-01')

    field = FieldMetaData(
        field="x",
        values=[second, first],
        type="datetime",
        strategies=[LAST_DATETIME]
    )

    mvs = MaxDateTimeStrategy(Dotty({}), field)
    assert mvs.prerequisites()
    assert mvs.merge().value.year == 2023

    first =  ValueTimestamp(value={})
    second =  ValueTimestamp(value='2023-01-01')

    field = FieldMetaData(
        field="x",
        values=[second, first],
        type="datetime",
        strategies=[LAST_DATETIME]
    )
    mvs = MaxDateTimeStrategy(Dotty({}), field)
    assert not mvs.prerequisites()