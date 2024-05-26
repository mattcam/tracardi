from dotty_dict import Dotty
from typing import List, Optional

from tracardi.service.merging.new.value_timestamp import ValueTimestamp
from tracardi.service.setup.mappings.objects.profile import default_profile_properties


class DictStrategy:

    def __init__(self, profiles: List[Dotty], field_metadata):
        self.profiles = profiles
        self.field_metadata = field_metadata

    def prerequisites(self) -> bool:
        for value_meta in self.field_metadata.values:  # List[FieldRef]
            if value_meta.value is None:
                continue
            if not isinstance(value_meta.value, dict):
                return False
        return True


class NestedStrategy(DictStrategy):

    def merge(self) -> Optional[ValueTimestamp]:
        # Skip Nones
        data = [value_meta for value_meta in self.field_metadata.values if value_meta.value is not None]
        print('----------------------')
        print(12,[value_meta.value for value_meta in self.field_metadata.values])
        print()

        from tracardi.service.merging.new.field_manager import FieldManager
        fm = FieldManager([Dotty({"id": id, self.field_metadata.field: value_meta.value}) for id, value_meta in enumerate(self.field_metadata.values)])
        print(fm._profiles)
        profile_metadata = fm.get_profiles_metadata(default_profile_properties, path=self.field_metadata.field)

        try:
            for field_meta, merged_value in profile_metadata.merge():
                print(field_meta.field, merged_value)

        except ValueError as e:
            print("Cant", str(e))

        # Filter out tuples with None
        # data = [value for value in data if value is not None]
        #
        print('----------------------')
        return ValueTimestamp(value=any(data))