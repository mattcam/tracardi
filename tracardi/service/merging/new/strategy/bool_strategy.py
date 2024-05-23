from typing import Optional

from tracardi.service.merging.new.field_ref import FieldRef


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
        for field_ref in self.field_merger.values:  # List[FieldRef]
            if not isinstance(field_ref.value, (bool, int, str)):
                return False
        return True


class AlwaysTrueStrategy(BoolStrategy):

    def merge(self) -> Optional[FieldRef]:
        # Return the first tuple in the sorted list
        return FieldRef(None, None, True, None)


class AlwaysFalseStrategy(BoolStrategy):

    def merge(self) -> Optional[FieldRef]:
        # Return the first tuple in the sorted list
        return FieldRef(None, None, False, None)


class OrStrategy(BoolStrategy):

    def merge(self) -> Optional[FieldRef]:
        # Convert all to datetime
        data = [convert_bool(field_ref.value) for field_ref in self.field_merger.values]
        # Filter out tuples with None
        data = [value for value in data if value is not None]

        return FieldRef(None, None, any(data), None)


class AndStrategy(BoolStrategy):

    def merge(self) -> Optional[FieldRef]:
        # Convert all to datetime
        data = [convert_bool(field_ref.value) for field_ref in self.field_merger.values]
        # Filter out tuples with None
        data = [value for value in data if value is not None]

        return FieldRef(None, None, all(data), None)
