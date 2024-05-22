import pytest
from datetime import datetime, timedelta

import time

from tracardi.service.merging.new.field_merger import FieldMerger
from tracardi.service.merging.new.merging_strategy_types import FIRST_UPDATE, LAST_UPDATE, MIN


def test_field_merger():
    first = ('1', datetime.now()-timedelta(seconds=100))
    second = ('2', time.time())
    field = FieldMerger(
        field="x",
        values=[second, first],
        type="string",
        strategies=[FIRST_UPDATE]
    )

    assert field.merge().value == first[0]
    field.strategies=[LAST_UPDATE]
    assert field.merge().value == second[0]
    field.values = [('1', None), ('2', time.time())]
    with pytest.raises(ValueError):
        field.merge()


def test_field_merger_fail_over():
    first = (20, datetime.now()-timedelta(seconds=100))
    second = (12.3, None)
    field = FieldMerger(
        field="x",
        values=[second, first],
        type="string",
        strategies=[FIRST_UPDATE, MIN]
    )

    assert field.merge().value == second[0]
    assert field.merge().strategy_id == MIN