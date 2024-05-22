from tracardi.service.merging.new.utils.converter import _convert


class ValueStrategy:

    def __init__(self, field_merger):
        self.field_merger = field_merger

    def prerequisites(self) -> bool:
        # Checks if the prerequisite of all items being numbers. Cant select min value if there is numbers.
        for field, _ in self.field_merger.values:
            if not isinstance(field, (int, float)):
                return False
        return True

class MinValueStrategy(ValueStrategy):

    def merge(self):
        # Filter out tuples with None as the fist (value) element
        filtered_data = [(x, y) for x, y in self.field_merger.values if x is not None]

        # Sort the filtered data based on the second element
        sorted_data = min(filtered_data,
                          key=lambda item: item[0])

        # Return the first tuple in the sorted list
        return _convert(sorted_data)

class MaxValueStrategy(ValueStrategy):

    def merge(self):
        # Filter out tuples with None as the fist (value) element
        filtered_data = [(x, y) for x, y in self.field_merger.values if x is not None]

        # Sort the filtered data based on the second element
        sorted_data = max(filtered_data,
                          key=lambda item: item[0])

        # Return the first tuple in the sorted list
        return _convert(sorted_data)


class SumValueStrategy(ValueStrategy):

    def merge(self):
        # Filter out tuples with None as the fist (value) element
        filtered_data = [x for x, y in self.field_merger.values if x is not None]

        # Return the first tuple in the sorted list
        return sum(filtered_data), None


class AvgValueStrategy(ValueStrategy):

    def merge(self):
        # Filter out tuples with None as the fist (value) element
        filtered_data = [x for x, y in self.field_merger.values if x is not None]

        # Return the first tuple in the sorted list
        return sum(filtered_data)/len(filtered_data), None