from datetime import datetime, timedelta
import time

from tracardi.service.merging.new.field_merger import FieldMerger
from tracardi.service.merging.new.field_ref import FieldRef
from tracardi.service.merging.new.merging_strategy_types import FIRST_UPDATE, LAST_UPDATE
from tracardi.service.merging.new.strategy.value_update_strategy import FirstUpdateStrategy, LastUpdateStrategy


def test_first_update_strategy():
    field = FieldMerger(
        field="x",
        values=[FieldRef(None, None, '1', None), FieldRef(None, None, '2', None)],
        type="number",
        strategies=[FIRST_UPDATE]
    )

    mvs = FirstUpdateStrategy(field)
    assert not mvs.prerequisites()

    ts1 = time.time()
    ts2 = datetime.now() - timedelta(seconds=100)

    first = FieldRef(None, None, '1', ts2)
    second = FieldRef(None, None, '2', ts1)

    field = FieldMerger(
        field="x",
        values=[second, first],
        type="number",
        strategies=[FIRST_UPDATE]
    )

    mvs = FirstUpdateStrategy(field)
    assert mvs.prerequisites()
    assert mvs.merge().value == '1'
    assert mvs.merge().timestamp ==  ts2.timestamp()


def test_last_update_strategy():
    field = FieldMerger(
        field="x",
        values=[FieldRef(None, None, '1', None), FieldRef(None, None, '2', None)],
        type="number",
        strategies=[LAST_UPDATE]
    )

    mvs = LastUpdateStrategy(field)
    assert not mvs.prerequisites()

    ts1 = time.time()
    ts2 = datetime.now() - timedelta(seconds=100)

    first = FieldRef(None, None, '1', ts2)
    second = FieldRef(None, None, '2', ts1)

    field = FieldMerger(
        field="x",
        values=[second, first],
        type="number",
        strategies=[LAST_UPDATE]
    )

    mvs = LastUpdateStrategy(field)
    assert mvs.prerequisites()
    assert mvs.merge() == second