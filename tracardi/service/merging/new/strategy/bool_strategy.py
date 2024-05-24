from dotty_dict import Dotty
from typing import Optional

from tracardi.service.merging.new.value_timestamp import ValueTimestamp


def convert_bool(value) -> Optional[bool]:
    if isinstance(value, bool):
        return value

    if isinstance(value, int):
        return value == 1

    if isinstance(value, str):
        return value.lower() in ['1', 'yes', 'true', 'on']

    return None


class BoolStrategy:

    def __init__(self, profile: Dotty, field_metadata):
        self.profile = profile
        self.field_metadata = field_metadata

    def prerequisites(self) -> bool:
        for value_meta in self.field_metadata.values:  # List[ValueTimestamp]
            if not isinstance(value_meta.value, (bool, int, str)):
                return False
        return True


class AlwaysTrueStrategy(BoolStrategy):

    def merge(self) -> Optional[ValueTimestamp]:
        # Return the first tuple in the sorted list
        return ValueTimestamp(value=True)


class AlwaysFalseStrategy(BoolStrategy):

    def merge(self) -> Optional[ValueTimestamp]:
        # Return the first tuple in the sorted list
        return ValueTimestamp(value=False)


class OrStrategy(BoolStrategy):

    def merge(self) -> Optional[ValueTimestamp]:
        # Convert all to datetime
        data = [convert_bool(value_meta.value) for value_meta in self.field_metadata.values]
        # Filter out tuples with None
        data = [value for value in data if value is not None]

        return ValueTimestamp(value=any(data))


class AndStrategy(BoolStrategy):

    def merge(self) -> Optional[ValueTimestamp]:
        # Convert all to datetime
        data = [convert_bool(value_meta.value) for value_meta in self.field_metadata.values]
        # Filter out tuples with None
        data = [value for value in data if value is not None]

        return ValueTimestamp(value=all(data))
