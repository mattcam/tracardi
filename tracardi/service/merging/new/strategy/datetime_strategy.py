from typing import Optional

from dateparser import parse
from datetime import datetime

from tracardi.service.merging.new.field_ref import FieldRef
from tracardi.service.merging.new.utils.converter import _convert


def convert_time(value) -> Optional[datetime]:
    if isinstance(value, datetime):
        return value

    if isinstance(value, float):
        return datetime.fromtimestamp(value)

    if isinstance(value, str):
        return parse(value)

    return None

class DateTimeStrategy:

    def __init__(self, field_merger):
        self.field_merger = field_merger

    def prerequisites(self) -> bool:
        # Checks if the prerequisite of all items being numbers. Cant select min value if there is numbers.
        for field_ref in self.field_merger.values:
            if not isinstance(field_ref.value, (datetime, float, str)):
                return False
        return True

class MinDateTimeStrategy(DateTimeStrategy):


    def merge(self):
        # Convert all to datetime
        data = [FieldRef(field_ref.profile, field_ref.field, convert_time(field_ref.value), field_ref.timestamp) for field_ref in self.field_merger.values]

        # Filter out tuples with None as the fist (value) element
        filtered_data = [field_ref for field_ref in data if field_ref.value is not None]

        # Sort the filtered data based on the second element
        sorted_data = min(filtered_data, key=lambda field_ref: field_ref.value)

        # Return the first tuple in the sorted list
        return _convert(sorted_data)


class MaxDateTimeStrategy(DateTimeStrategy):


    def merge(self):
        # Convert all to datetime
        data = [FieldRef(field_ref.profile, field_ref.field, convert_time(field_ref.value), field_ref.timestamp) for
                field_ref in self.field_merger.values]

        # Filter out tuples with None as the fist (value) element
        filtered_data = [field_ref for field_ref in data if field_ref.value is not None]

        # Sort the filtered data based on the second element
        sorted_data = max(filtered_data, key=lambda field_ref: field_ref.value)

        # Return the first tuple in the sorted list
        return _convert(sorted_data)

