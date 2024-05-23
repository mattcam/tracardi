from tracardi.service.merging.new.field_merger import FieldMerger
from tracardi.service.merging.new.field_ref import FieldRef
from tracardi.service.merging.new.merging_strategy_types import MIN, MAX
from tracardi.service.merging.new.strategy.list_strategy import ConCatStrategy, ConCatDistinctStrategy
from tracardi.service.merging.new.strategy.value_strategy import MinValueStrategy, MaxValueStrategy, SumValueStrategy


def test_list_extend_strategy():
    field = FieldMerger(
        field="x",
        values=[FieldRef(None, None, '1', None), FieldRef(None, None, '2', None)],
        type="number",
        strategies=[MIN]
    )

    mvs = ConCatStrategy(field)
    assert not mvs.prerequisites()

    field = FieldMerger(
        field="x",
        values=[FieldRef(None, None, [10, 'a'], None), FieldRef(None, None, [2.3, 10], None)],
        type="number",
        strategies=[MIN]
    )

    mvs = ConCatStrategy(field)
    assert mvs.prerequisites()
    assert mvs.merge() == FieldRef(None, None, [10, 'a', 2.3, 10], None)

def test_list_extend_uniq_strategy():
    field = FieldMerger(
        field="x",
        values=[FieldRef(None, None, '1', None), FieldRef(None, None, '2', None)],
        type="number",
        strategies=[MIN]
    )

    mvs = ConCatDistinctStrategy(field)
    assert not mvs.prerequisites()

    field = FieldMerger(
        field="x",
        values=[FieldRef(None, None, [10, 'a'], None), FieldRef(None, None, [2.3, 10], None)],
        type="number",
        strategies=[MIN]
    )

    mvs = ConCatDistinctStrategy(field)
    assert mvs.prerequisites()
    assert mvs.merge() == FieldRef(None, None, [10, 'a', 2.3], None)