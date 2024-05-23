from typing import Optional

from datetime import datetime

from tracardi.service.merging.new.field_ref import FieldRef
from tracardi.service.merging.new.utils.converter import _convert


class ValueUpdateStrategy:

    def __init__(self, field_merger):
        self.field_merger = field_merger

    def prerequisites(self) -> bool:
        # Checks if the prerequisite of all items having timestamp is met. Cant select last update if there is no timestamps on all fields.
        for field_ref in self.field_merger.values:
            if not field_ref.timestamp:
                return False
        return True

class LastUpdateStrategy(ValueUpdateStrategy):

    def merge(self) -> Optional[FieldRef]:
        # Filter out tuples with None as the second element and convert
        filtered_data = [FieldRef(
            field_ref.profile,
            field_ref.field,
            field_ref.value,
            field_ref.timestamp.timestamp() if isinstance(field_ref.timestamp, datetime) else field_ref.timestamp)
            for field_ref in self.field_merger.values if field_ref.timestamp is not None]

        # Sort the filtered data based on the second element
        sorted_data = max(filtered_data, key=lambda field_ref: field_ref.timestamp)

        # Return the first tuple in the sorted list
        return _convert(sorted_data)


class FirstUpdateStrategy(ValueUpdateStrategy):

    def merge(self) -> Optional[FieldRef]:
        # Filter out tuples with None as the second element and convert
        filtered_data = [FieldRef(
            field_ref.profile,
            field_ref.field,
            field_ref.value,
            field_ref.timestamp.timestamp() if isinstance(field_ref.timestamp, datetime) else field_ref.timestamp)
            for field_ref in self.field_merger.values if field_ref.timestamp is not None]

        # Sort the filtered data based on the second element
        sorted_data = min(filtered_data, key=lambda field_ref: field_ref.timestamp)

        # Return the first tuple in the sorted list
        return _convert(sorted_data)