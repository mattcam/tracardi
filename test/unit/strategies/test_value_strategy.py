import pytest

from tracardi.service.merging.new.field_merger import FieldMerger
from tracardi.service.merging.new.merging_strategy_types import MIN
from tracardi.service.merging.new.strategy.value_strategy import MinValueStrategy


def test_min_value_strategy():
    field = FieldMerger(
        field="x",
        values=[('1', None), ('2', None)],
        type="number",
        strategies=[MIN]
    )

    mvs = MinValueStrategy(field)
    assert not mvs.prerequisites()

    field = FieldMerger(
        field="x",
        values=[(10, None), (2.3, None)],
        type="number",
        strategies=[MIN]
    )

    mvs = MinValueStrategy(field)
    assert mvs.prerequisites()
    assert mvs.merge() == (2.3, None)


def test_max_value_strategy():
    field = FieldMerger(
        field="x",
        values=[('1', None), ('2', None)],
        type="number",
        strategies=[MIN]
    )

    mvs = MaxValueStrategy(field)
    assert not mvs.prerequisites()

    field = FieldMerger(
        field="x",
        values=[(10, None), (2.3, None)],
        type="number",
        strategies=[MIN]
    )

    mvs = MaxValueStrategy(field)
    assert mvs.prerequisites()
    assert mvs.merge() == (10, None)


def test_sum_value_strategy():
    field = FieldMerger(
        field="x",
        values=[('1', None), ('2', None)],
        type="number",
        strategies=[MIN]
    )

    mvs = SumValueStrategy(field)
    assert not mvs.prerequisites()

    field = FieldMerger(
        field="x",
        values=[(10, None), (2.3, None)],
        type="number",
        strategies=[MIN]
    )

    mvs = SumValueStrategy(field)
    assert mvs.prerequisites()
    assert mvs.merge() == (12.3, None)