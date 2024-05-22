from typing import Optional

from dateparser import parse
from datetime import datetime

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
        for value, _ in self.field_merger.values:
            if not isinstance(value, (datetime, float, str)):
                return False
        return True

class MinDateTimeStrategy(DateTimeStrategy):


    def merge(self):
        # Convert all to datetime
        data = [(convert_time(value), timestamp) for value, timestamp in self.field_merger.values]

        # Filter out tuples with None as the fist (value) element
        filtered_data = [(value, timestamp) for value, timestamp in data if value is not None]

        # Sort the filtered data based on the second element
        sorted_data = min(filtered_data, key=lambda item: item[0])

        # Return the first tuple in the sorted list
        return _convert(sorted_data)


class MaxDateTimeStrategy(DateTimeStrategy):


    def merge(self):
        # Convert all to datetime
        data = [(convert_time(value), timestamp) for value, timestamp in self.field_merger.values]

        # Filter out tuples with None as the fist (value) element
        filtered_data = [(value, timestamp) for value, timestamp in data if value is not None]

        # Sort the filtered data based on the second element
        sorted_data = max(filtered_data, key=lambda item: item[0])

        # Return the first tuple in the sorted list
        return _convert(sorted_data)

