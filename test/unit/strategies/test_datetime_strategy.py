from tracardi.service.merging.new.field_merger import FieldMerger
from tracardi.service.merging.new.field_ref import FieldRef
from tracardi.service.merging.new.merging_strategy_types import FIRST_DATETIME, LAST_DATETIME
from tracardi.service.merging.new.strategy.datetime_strategy import MinDateTimeStrategy, MaxDateTimeStrategy


def test_first_datetime_strategy():
    first = FieldRef(None, None, '2004-01-18T17:13:28.620880Z', None)
    second =  FieldRef(None, None, '2024-05-18T17:13:28.620880+00:00', None)
    third =  FieldRef(None, None, '2024-05-18T17:13:28.620880+00:00', None)

    field = FieldMerger(
        field="x",
        values=[second, first],
        type="datetime",
        strategies=[FIRST_DATETIME]
    )

    mvs = MinDateTimeStrategy(field)
    assert mvs.prerequisites()
    assert mvs.merge().value.year == 2004

    first = FieldRef(None, None, {}, None)
    second = FieldRef(None, None, '2023-01-01', None)

    field = FieldMerger(
        field="x",
        values=[third, second, first],
        type="datetime",
        strategies=[FIRST_DATETIME]
    )
    mvs = MinDateTimeStrategy(field)
    assert not mvs.prerequisites()



def test_last_datetime_strategy():
    first =  FieldRef(None, None, '2002-01-01', None)
    second =  FieldRef(None, None, '2023-01-01', None)

    field = FieldMerger(
        field="x",
        values=[second, first],
        type="datetime",
        strategies=[LAST_DATETIME]
    )

    mvs = MaxDateTimeStrategy(field)
    assert mvs.prerequisites()
    assert mvs.merge().value.year == 2023

    first =  FieldRef(None, None, {}, None)
    second =  FieldRef(None, None, '2023-01-01', None)

    field = FieldMerger(
        field="x",
        values=[second, first],
        type="datetime",
        strategies=[LAST_DATETIME]
    )
    mvs = MaxDateTimeStrategy(field)
    assert not mvs.prerequisites()