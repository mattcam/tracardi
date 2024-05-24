from dotty_dict import Dotty

from tracardi.service.merging.new.field_metadata import FieldMetaData
from tracardi.service.merging.new.merging_strategy_types import LAST_PROFILE_INSERT_TIME
from tracardi.service.merging.new.strategy.profile_datetime_strategy import LastProfileInsertTimeStrategy, \
    LastProfileUpdateTimeStrategy
from tracardi.service.merging.new.value_timestamp import ValueTimestamp


def test_max_profile_insert_time_strategy():
    field = FieldMetaData(
        field="x",
        values=[
            ValueTimestamp(profile_insert='abc', value='1'),
            ValueTimestamp(profile_insert='2020-01-01', value='2')
        ],
        type="number",
        strategies=[LAST_PROFILE_INSERT_TIME]
    )
    mvs = LastProfileInsertTimeStrategy(Dotty({}), field)
    assert not mvs.prerequisites()

    second = ValueTimestamp(profile_insert='2021-01-01', value='2')
    field = FieldMetaData(
        field="x",
        values=[ValueTimestamp(profile_insert='2020-01-01', value='1'), second],
        type="number",
        strategies=[LAST_PROFILE_INSERT_TIME]
    )

    mvs = LastProfileInsertTimeStrategy(Dotty({}), field)
    assert mvs.prerequisites()

    assert mvs.merge() == second


def test_max_profile_update_time_strategy():
    field = FieldMetaData(
        field="x",
        values=[
            ValueTimestamp(profile_update='abc', value='1'),
            ValueTimestamp(profile_update='2020-01-01', value='2')
        ],
        type="number",
        strategies=[LAST_PROFILE_INSERT_TIME]
    )

    mvs = LastProfileUpdateTimeStrategy(Dotty({}), field)
    assert not mvs.prerequisites()

    second = ValueTimestamp(profile_update='2021-01-01', value='2')
    field = FieldMetaData(
        field="x",
        values=[ValueTimestamp(profile_update='2020-01-01', value='1'), second],
        type="number",
        strategies=[LAST_PROFILE_INSERT_TIME]
    )

    mvs = LastProfileUpdateTimeStrategy(Dotty({}), field)
    assert mvs.prerequisites()

    assert mvs.merge() == second
