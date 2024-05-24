from dotty_dict import Dotty
from typing import Optional

from tracardi.service.merging.new.value_timestamp import ValueTimestamp


class DictStrategy:

    def __init__(self, profile: Dotty, field_metadata):
        self.profile = profile
        self.field_metadata = field_metadata

    def prerequisites(self) -> bool:
        for field_ref in self.field_metadata.values:  # List[FieldRef]
            if not isinstance(field_ref.value, dict):
                return False
        return True


class NestedStrategy(DictStrategy):

    def merge(self) -> Optional[ValueTimestamp]:
        # Skip Nones
        data = [field_ref for field_ref in self.field_metadata.values if field_ref.value is not None]

        print([field_ref.value for field_ref in self.field_metadata.values])

        # fm = self.field_merger.get_profiles_metadata({}, path="x")

        # Filter out tuples with None
        # data = [value for value in data if value is not None]
        #
        return ValueTimestamp(value=any(data))