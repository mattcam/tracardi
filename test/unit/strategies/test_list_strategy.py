from dotty_dict import Dotty

from tracardi.service.merging.new.field_metadata import FieldMetaData
from tracardi.service.merging.new.merging_strategy_types import MIN
from tracardi.service.merging.new.strategy.list_strategy import ConCatStrategy, ConCatDistinctStrategy
from tracardi.service.merging.new.value_timestamp import ValueTimestamp


def test_list_extend_strategy():
    field = FieldMetaData(
        field="x",
        values=[ValueTimestamp(value='1'), ValueTimestamp(value='2')],
        type="number",
        strategies=[MIN]
    )

    mvs = ConCatStrategy(Dotty({}), field)
    assert not mvs.prerequisites()

    field = FieldMetaData(
        field="x",
        values=[ValueTimestamp(value=[10, 'a']), ValueTimestamp(value=[2.3, 10])],
        type="number",
        strategies=[MIN]
    )

    mvs = ConCatStrategy(Dotty({}), field)
    assert mvs.prerequisites()
    assert mvs.merge() == ValueTimestamp(value=[10, 'a', 2.3, 10])

def test_list_extend_uniq_strategy():
    field = FieldMetaData(
        field="x",
        values=[ValueTimestamp(value='1'), ValueTimestamp(value='2')],
        type="number",
        strategies=[MIN]
    )

    mvs = ConCatDistinctStrategy(Dotty({}), field)
    assert not mvs.prerequisites()

    field = FieldMetaData(
        field="x",
        values=[ValueTimestamp(value=[10, 'a']), ValueTimestamp(value=[2.3, 10])],
        type="number",
        strategies=[MIN]
    )

    mvs = ConCatDistinctStrategy(Dotty({}), field)
    assert mvs.prerequisites()
    assert set(mvs.merge().value) == {10, 'a', 2.3}