import pytest
from datetime import datetime, timedelta

import time
from dotty_dict import Dotty

from tracardi.service.merging.new.field_metadata import FieldMetaData
from tracardi.service.merging.new.merging_strategy_types import FIRST_UPDATE, LAST_UPDATE, MIN
from tracardi.service.merging.new.value_timestamp import ValueTimestamp


def test_field_merger():
    first = ValueTimestamp(value='1', timestamp=datetime.now()-timedelta(seconds=100))
    second = ValueTimestamp(value='2', timestamp=time.time())
    field = FieldMetaData(
        field="x",
        values=[second, first],
        type="string",
        strategies=[FIRST_UPDATE]
    )

    assert field.merge([Dotty({})], []).value == first.value
    field.strategies=[LAST_UPDATE]
    assert field.merge([Dotty({})], []).value == second.value
    field.values = [ValueTimestamp(value='1'), ValueTimestamp(value='2', timestamp=time.time())]
    with pytest.raises(ValueError):
        field.merge([Dotty({})], [])


def test_field_merger_fail_over():
    first = ValueTimestamp(value=20, timestamp=datetime.now()-timedelta(seconds=100))
    second = ValueTimestamp(value=12.3)
    field = FieldMetaData(
        field="x",
        values=[second, first],
        type="string",
        strategies=[FIRST_UPDATE, MIN]
    )

    assert field.merge([Dotty({})], []).value == second.value
    assert field.merge([Dotty({})], []).strategy_id == MIN