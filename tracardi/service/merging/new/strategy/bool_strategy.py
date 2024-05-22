from typing import Optional

def convert_bool(value) -> Optional[bool]:
    if isinstance(value, bool):
        return value

    if isinstance(value, int):
        return value == 1

    if isinstance(value, str):
        return value.lower() in ['1', 'yes', 'true', 'on']

    return None

class BoolStrategy:

    def __init__(self, field_merger):
        self.field_merger = field_merger

    def prerequisites(self) -> bool:
        for value, _ in self.field_merger.values:
            if not isinstance(value, (bool, int, str)):
                return False
        return True


class AlwaysTrueStrategy(BoolStrategy):

    def merge(self):
        # Return the first tuple in the sorted list
        return True, None

class AlwaysFalseStrategy(BoolStrategy):

    def merge(self):
        # Return the first tuple in the sorted list
        return False, None

class OrStrategy(BoolStrategy):

    def merge(self):
        # Convert all to datetime
        data = [convert_bool(value) for value, timestamp in self.field_merger.values]
        # Filter out tuples with None
        data = [value for value in data if value is not None]

        return any(data), None


class AndStrategy(BoolStrategy):

    def merge(self):
        # Convert all to datetime
        data = [convert_bool(value) for value, timestamp in self.field_merger.values]
        # Filter out tuples with None
        data = [value for value in data if value is not None]

        return all(data), None