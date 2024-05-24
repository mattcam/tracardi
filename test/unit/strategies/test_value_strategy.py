from dotty_dict import Dotty

from tracardi.service.merging.new.field_metadata import FieldMetaData
from tracardi.service.merging.new.merging_strategy_types import MIN, MAX
from tracardi.service.merging.new.strategy.value_strategy import MinValueStrategy, MaxValueStrategy, SumValueStrategy
from tracardi.service.merging.new.value_timestamp import ValueTimestamp


def test_min_value_strategy():
    field = FieldMetaData(
        field="x",
        values=[ValueTimestamp(value='1'), ValueTimestamp(value='2')],
        type="number",
        strategies=[MIN]
    )

    mvs = MinValueStrategy(Dotty({}), field)
    assert not mvs.prerequisites()

    field = FieldMetaData(
        field="x",
        values=[ValueTimestamp(value=10), ValueTimestamp(value=2.3)],
        type="number",
        strategies=[MIN]
    )

    mvs = MinValueStrategy(Dotty({}), field)
    assert mvs.prerequisites()
    assert mvs.merge() == ValueTimestamp(value=2.3)


def test_max_value_strategy():
    field = FieldMetaData(
        field="x",
        values=[ValueTimestamp(value='1'), ValueTimestamp(value='2')],
        type="number",
        strategies=[MAX]
    )

    mvs = MaxValueStrategy(Dotty({}), field)
    assert not mvs.prerequisites()

    field = FieldMetaData(
        field="x",
        values=[ValueTimestamp(value=10), ValueTimestamp(value=2.3)],
        type="number",
        strategies=[MAX]
    )

    mvs = MaxValueStrategy(Dotty({}), field)
    assert mvs.prerequisites()
    assert mvs.merge() == ValueTimestamp(value=10)


def test_sum_value_strategy():
    field = FieldMetaData(
        field="x",
        values=[ValueTimestamp(value='1'), ValueTimestamp(value='2')],
        type="number",
        strategies=[MIN]
    )

    mvs = SumValueStrategy(Dotty({}), field)
    assert not mvs.prerequisites()

    field = FieldMetaData(
        field="x",
        values=[ValueTimestamp(value=10), ValueTimestamp(value=2.3)],
        type="number",
        strategies=[MIN]
    )

    mvs = SumValueStrategy(Dotty({}), field)
    assert mvs.prerequisites()
    assert mvs.merge() == ValueTimestamp(value=12.3)