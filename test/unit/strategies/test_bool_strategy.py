from dotty_dict import Dotty

from tracardi.service.merging.new.field_metadata import FieldMetaData
from tracardi.service.merging.new.merging_strategy_types import ALWAYS_TRUE, ALWAYS_FALSE, AND, OR
from tracardi.service.merging.new.strategy.bool_strategy import AlwaysTrueStrategy, AlwaysFalseStrategy, \
    AndStrategy, OrStrategy
from tracardi.service.merging.new.value_timestamp import ValueTimestamp


def test_always_true_strategy():
    field = FieldMetaData(
        field="x",
        values=[ValueTimestamp(value='1'), ValueTimestamp(value='2')],
        type="number",
        strategies=[ALWAYS_TRUE]
    )

    mvs = AlwaysTrueStrategy(Dotty({}), field)
    assert mvs.prerequisites()  # It is true as only types are checked

    assert mvs.merge() == ValueTimestamp(value=True)

    field = FieldMetaData(
        field="x",
        values=[ValueTimestamp(value=True), ValueTimestamp(value='0')],
        type="number",
        strategies=[ALWAYS_TRUE]
    )

    mvs = AlwaysTrueStrategy(Dotty({}), field)
    assert mvs.prerequisites()
    assert mvs.merge() == ValueTimestamp(value=True)


def test_always_false_strategy():
    field = FieldMetaData(
        field="x",
        values=[ValueTimestamp(value='1'), ValueTimestamp(value='2')],
        type="number",
        strategies=[ALWAYS_FALSE]
    )

    mvs = AlwaysFalseStrategy(Dotty({}), field)
    assert mvs.prerequisites()  # It is true as only types are checked

    assert mvs.merge() == ValueTimestamp(value=False)

    field = FieldMetaData(
        field="x",
        values=[ValueTimestamp(value=True), ValueTimestamp(value='0')],
        type="number",
        strategies=[ALWAYS_FALSE]
    )

    mvs = AlwaysFalseStrategy(Dotty({}), field)
    assert mvs.prerequisites()
    assert mvs.merge() == ValueTimestamp(value=False)


def test_and_strategy():
    field = FieldMetaData(
        field="x",
        values=[ValueTimestamp(value='1'), ValueTimestamp(value=None)],
        type="number",
        strategies=[AND]
    )

    mvs = AndStrategy(Dotty({}), field)
    assert not mvs.prerequisites()

    # Skips none values
    assert mvs.merge() == ValueTimestamp(value=True)

    field = FieldMetaData(
        field="x",
        values=[ValueTimestamp(value=True), ValueTimestamp(value='0')],
        type="number",
        strategies=[AND]
    )

    mvs = AndStrategy(Dotty({}), field)
    assert mvs.prerequisites()
    assert mvs.merge() == ValueTimestamp(value=False)


def test_or_strategy():
    field = FieldMetaData(
        field="x",
        values=[ValueTimestamp(value='1'), ValueTimestamp(value=None)],
        type="number",
        strategies=[OR]
    )

    mvs = OrStrategy(Dotty({}), field)
    assert not mvs.prerequisites()

    # Skips none values
    assert mvs.merge() == ValueTimestamp(value=True)

    field = FieldMetaData(
        field="x",
        values=[ValueTimestamp(value=True), ValueTimestamp(value='0')],
        type="number",
        strategies=[OR]
    )

    mvs = OrStrategy(Dotty({}), field)
    assert mvs.prerequisites()
    assert mvs.merge() == ValueTimestamp(value=True)
