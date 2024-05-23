from typing import Optional

from tracardi.service.merging.new.field_ref import FieldRef
from tracardi.service.merging.new.utils.converter import _convert


class ValueStrategy:

    def __init__(self, field_merger):
        self.field_merger = field_merger

    def prerequisites(self) -> bool:
        # Checks if the prerequisite of all items being numbers. Cant select min value if there is numbers.
        for field_ref in self.field_merger.values:
            if not isinstance(field_ref.value, (int, float)):
                return False
        return True


class MinValueStrategy(ValueStrategy):

    def merge(self) -> Optional[FieldRef]:
        # Filter out tuples with None as the fist (value) element
        filtered_data = [field_ref for field_ref in self.field_merger.values if field_ref.value is not None]

        sorted_data = min(filtered_data, key=lambda field_ref: field_ref.value)

        # Return the first tuple in the sorted list
        return _convert(sorted_data)


class MaxValueStrategy(ValueStrategy):

    def merge(self) -> Optional[FieldRef]:
        # Filter out tuples with None as the fist (value) element
        filtered_data = [field_ref for field_ref in self.field_merger.values if field_ref.value is not None]

        sorted_data = max(filtered_data, key=lambda field_ref: field_ref.value)

        # Return the first tuple in the sorted list
        return _convert(sorted_data)


class SumValueStrategy(ValueStrategy):

    def merge(self) -> Optional[FieldRef]:
        # Filter out tuples with None as the fist (value) element
        filtered_data = [field_ref.value for field_ref in self.field_merger.values if field_ref.value is not None]

        # Return the first tuple in the sorted list
        return FieldRef(None, None, sum(filtered_data), None)


class AvgValueStrategy(ValueStrategy):

    def merge(self) -> Optional[FieldRef]:
        # Filter out tuples with None as the fist (value) element
        filtered_data = [field_ref.value for field_ref in self.field_merger.values if field_ref.value is not None]

        # Return the first tuple in the sorted list
        return FieldRef(None, None, sum(filtered_data) / len(filtered_data), None)
