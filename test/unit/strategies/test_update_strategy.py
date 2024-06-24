from datetime import datetime, timedelta
import time
from dotty_dict import Dotty

from tracardi.service.merging.new.field_metadata import FieldMetaData
from tracardi.service.merging.new.merging_strategy_types import FIRST_UPDATE, LAST_UPDATE
from tracardi.service.merging.new.strategy.value_update_strategy import FirstUpdateStrategy, LastUpdateStrategy
from tracardi.service.merging.new.value_timestamp import ValueTimestamp


def test_first_update_strategy():
    field = FieldMetaData(
        field="x",
        values=[ValueTimestamp(value= '1'), ValueTimestamp(value= '2')],
        type="number",
        strategies=[FIRST_UPDATE]
    )

    mvs = FirstUpdateStrategy(Dotty({}), field)
    assert not mvs.prerequisites()

    ts1 = time.time()
    ts2 = datetime.now() - timedelta(seconds=100)

    first = ValueTimestamp(value= '1', timestamp=ts2)
    second = ValueTimestamp(value= '2', timestamp=ts1)

    field = FieldMetaData(
        field="x",
        values=[second, first],
        type="number",
        strategies=[FIRST_UPDATE]
    )

    mvs = FirstUpdateStrategy(Dotty({}), field)
    assert mvs.prerequisites()
    assert mvs.merge().value == '1'
    assert mvs.merge().timestamp ==  ts2.timestamp()


def test_last_update_strategy():
    field = FieldMetaData(
        field="x",
        values=[ValueTimestamp(value= '1'), ValueTimestamp(value= '2')],
        type="number",
        strategies=[LAST_UPDATE]
    )

    mvs = LastUpdateStrategy(Dotty({}), field)
    assert not mvs.prerequisites()

    ts1 = time.time()
    ts2 = datetime.now() - timedelta(seconds=100)

    first = ValueTimestamp(value= '1', timestamp=ts2)
    second = ValueTimestamp(value= '2', timestamp=ts1)

    field = FieldMetaData(
        field="x",
        values=[second, first],
        type="number",
        strategies=[LAST_UPDATE]
    )

    mvs = LastUpdateStrategy(Dotty({}), field)
    assert mvs.prerequisites()
    assert mvs.merge() == second