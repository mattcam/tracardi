from datetime import datetime, timedelta
import time

import pytest

from tracardi.service.merging.new.field_merger import FieldMerger
from tracardi.service.merging.new.merging_strategy_types import FIRST_UPDATE, LAST_UPDATE
from tracardi.service.merging.new.strategy.value_update_strategy import FirstUpdateStrategy, LastUpdateStrategy


def test_first_update_strategy():
    field = FieldMerger(
        field="x",
        values=[('1', None), ('2', None)],
        type="number",
        strategies=[FIRST_UPDATE]
    )

    mvs = FirstUpdateStrategy(field)
    assert not mvs.prerequisites()

    ts1 = time.time()
    ts2 = datetime.now() - timedelta(seconds=100)

    first = ('1', ts2)
    second = ('2', ts1)

    field = FieldMerger(
        field="x",
        values=[second, first],
        type="number",
        strategies=[FIRST_UPDATE]
    )

    mvs = FirstUpdateStrategy(field)
    assert mvs.prerequisites()
    assert mvs.merge() == ('1', ts2.timestamp())


def test_last_update_strategy():
    field = FieldMerger(
        field="x",
        values=[('1', None), ('2', None)],
        type="number",
        strategies=[LAST_UPDATE]
    )

    mvs = LastUpdateStrategy(field)
    assert not mvs.prerequisites()

    ts1 = time.time()
    ts2 = datetime.now() - timedelta(seconds=100)

    first = ('1', ts2)
    second = ('2', ts1)

    field = FieldMerger(
        field="x",
        values=[second, first],
        type="number",
        strategies=[LAST_UPDATE]
    )

    mvs = LastUpdateStrategy(field)
    assert mvs.prerequisites()
    assert mvs.merge() == second