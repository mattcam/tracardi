from datetime import datetime

from tracardi.service.merging.new.utils.converter import _convert


class ValueUpdateStrategy:

    def __init__(self, field_merger):
        self.field_merger = field_merger

    def prerequisites(self) -> bool:
        # Checks if the prerequisite of all items having timestamp is met. Cant select last update if there is no timestamps on all fields.
        for field, timestamp in self.field_merger.values:
            if not timestamp:
                return False
        return True

class LastUpdateStrategy(ValueUpdateStrategy):

    def merge(self):
        # Filter out tuples with None as the second element and convert
        filtered_data = [(x, y.timestamp() if isinstance(y, datetime) else y) for x, y in self.field_merger.values if y is not None]

        # Sort the filtered data based on the second element
        sorted_data = max(filtered_data, key=lambda item: item[1])

        # Return the first tuple in the sorted list
        return _convert(sorted_data)


class FirstUpdateStrategy(ValueUpdateStrategy):

    def merge(self):
        # Filter out tuples with None as the second element and convert
        filtered_data = [(x, y.timestamp() if isinstance(y, datetime) else y) for x, y in self.field_merger.values if y is not None]

        # Sort the filtered data based on the second element
        sorted_data = min(filtered_data, key=lambda item: item[1])

        # Return the first tuple in the sorted list
        return _convert(sorted_data)