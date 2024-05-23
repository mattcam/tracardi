from tracardi.service.merging.new.field_merger import FieldMerger
from tracardi.service.merging.new.field_ref import FieldRef
from tracardi.service.merging.new.merging_strategy_types import MIN, MAX
from tracardi.service.merging.new.strategy.value_strategy import MinValueStrategy, MaxValueStrategy, SumValueStrategy


def test_min_value_strategy():
    field = FieldMerger(
        field="x",
        values=[FieldRef(None, None, '1', None), FieldRef(None, None, '2', None)],
        type="number",
        strategies=[MIN]
    )

    mvs = MinValueStrategy(field)
    assert not mvs.prerequisites()

    field = FieldMerger(
        field="x",
        values=[FieldRef(None, None, 10, None), FieldRef(None, None, 2.3, None)],
        type="number",
        strategies=[MIN]
    )

    mvs = MinValueStrategy(field)
    assert mvs.prerequisites()
    assert mvs.merge() == FieldRef(None, None, 2.3, None)


def test_max_value_strategy():
    field = FieldMerger(
        field="x",
        values=[FieldRef(None, None, '1', None), FieldRef(None, None, '2', None)],
        type="number",
        strategies=[MAX]
    )

    mvs = MaxValueStrategy(field)
    assert not mvs.prerequisites()

    field = FieldMerger(
        field="x",
        values=[FieldRef(None, None, 10, None), FieldRef(None, None, 2.3, None)],
        type="number",
        strategies=[MAX]
    )

    mvs = MaxValueStrategy(field)
    assert mvs.prerequisites()
    assert mvs.merge() == FieldRef(None, None, 10, None)


def test_sum_value_strategy():
    field = FieldMerger(
        field="x",
        values=[FieldRef(None, None, '1', None), FieldRef(None, None, '2', None)],
        type="number",
        strategies=[MIN]
    )

    mvs = SumValueStrategy(field)
    assert not mvs.prerequisites()

    field = FieldMerger(
        field="x",
        values=[FieldRef(None, None, 10, None), FieldRef(None, None, 2.3, None)],
        type="number",
        strategies=[MIN]
    )

    mvs = SumValueStrategy(field)
    assert mvs.prerequisites()
    assert mvs.merge() == FieldRef(None, None, 12.3, None)