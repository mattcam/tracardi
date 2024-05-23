import pytest

from tracardi.service.merging.new.field_merger import FieldMerger
from tracardi.service.merging.new.field_ref import FieldRef
from tracardi.service.merging.new.merging_strategy_types import MIN, MAX, ALWAYS_TRUE, ALWAYS_FALSE, AND, OR
from tracardi.service.merging.new.strategy.bool_strategy import BoolStrategy, AlwaysTrueStrategy, AlwaysFalseStrategy, \
    AndStrategy, OrStrategy
from tracardi.service.merging.new.strategy.value_strategy import MinValueStrategy, MaxValueStrategy, SumValueStrategy


def test_always_true_strategy():
    field = FieldMerger(
        field="x",
        values=[FieldRef(None, None, '1', None), FieldRef(None, None, '2', None)],
        type="number",
        strategies=[ALWAYS_TRUE]
    )

    mvs = AlwaysTrueStrategy(field)
    assert mvs.prerequisites()  # It is true as only types are checked

    assert mvs.merge() == FieldRef(None, None, True, None)

    field = FieldMerger(
        field="x",
        values=[FieldRef(None, None, True, None), FieldRef(None, None, '0', None)],
        type="number",
        strategies=[ALWAYS_TRUE]
    )

    mvs = AlwaysTrueStrategy(field)
    assert mvs.prerequisites()
    assert mvs.merge() == FieldRef(None, None, True, None)


def test_always_false_strategy():
    field = FieldMerger(
        field="x",
        values=[FieldRef(None, None, '1', None), FieldRef(None, None, '2', None)],
        type="number",
        strategies=[ALWAYS_FALSE]
    )

    mvs = AlwaysFalseStrategy(field)
    assert mvs.prerequisites()  # It is true as only types are checked

    assert mvs.merge() == FieldRef(None, None, False, None)

    field = FieldMerger(
        field="x",
        values=[FieldRef(None, None, True, None), FieldRef(None, None, '0', None)],
        type="number",
        strategies=[ALWAYS_FALSE]
    )

    mvs = AlwaysFalseStrategy(field)
    assert mvs.prerequisites()
    assert mvs.merge() == FieldRef(None, None, False, None)


def test_and_strategy():
    field = FieldMerger(
        field="x",
        values=[FieldRef(None, None, '1', None), FieldRef(None, None, None, None)],
        type="number",
        strategies=[AND]
    )

    mvs = AndStrategy(field)
    assert not mvs.prerequisites()

    # Skips none values
    assert mvs.merge() == FieldRef(None, None, True, None)

    field = FieldMerger(
        field="x",
        values=[FieldRef(None, None, True, None), FieldRef(None, None, '0', None)],
        type="number",
        strategies=[AND]
    )

    mvs = AndStrategy(field)
    assert mvs.prerequisites()
    assert mvs.merge() == FieldRef(None, None, False, None)


def test_or_strategy():
    field = FieldMerger(
        field="x",
        values=[FieldRef(None, None, '1', None), FieldRef(None, None, None, None)],
        type="number",
        strategies=[OR]
    )

    mvs = OrStrategy(field)
    assert not mvs.prerequisites()

    # Skips none values
    assert mvs.merge() == FieldRef(None, None, True, None)

    field = FieldMerger(
        field="x",
        values=[FieldRef(None, None, True, None), FieldRef(None, None, '0', None)],
        type="number",
        strategies=[OR]
    )

    mvs = OrStrategy(field)
    assert mvs.prerequisites()
    assert mvs.merge() == FieldRef(None, None, True, None)