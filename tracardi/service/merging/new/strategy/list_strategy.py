from itertools import chain

from typing import Optional

from tracardi.service.merging.new.field_ref import FieldRef
from tracardi.service.merging.new.utils.converter import _convert


def convert_list(value) -> Optional[list]:
    if isinstance(value, list):
        return value

    if isinstance(value, set):
        return list(value)

    return None


class ListStrategy:

    def __init__(self, field_merger):
        self.field_merger = field_merger

    def prerequisites(self) -> bool:
        for field_ref in self.field_merger.values:
            if not isinstance(field_ref.value, (list, set)):
                return False
        return True


class ConCatStrategy(ListStrategy):

    def merge(self):
        # Convert all to datetime
        data = [convert_list(field_ref.value) for field_ref in self.field_merger.values]

        # Filter out tuples with None as the fist (value) element
        filtered_data = [value for value in data if value is not None]

        return FieldRef(None, None, list(chain.from_iterable(filtered_data)), None)


class ConCatDistinctStrategy(ListStrategy):

    def merge(self):
        # Convert all to datetime
        data = [convert_list(field_ref.value) for field_ref in self.field_merger.values]

        # Filter out tuples with None as the fist (value) element
        filtered_data = [value for value in data if value is not None]

        return FieldRef(None, None, list(set((chain.from_iterable(filtered_data)))), None)
