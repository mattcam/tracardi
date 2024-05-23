from collections import defaultdict
from typing import List, Tuple, Dict, Set

from pprint import pprint

from datetime import datetime
from dotty_dict import Dotty
from tracardi.process_engine.tql.utils.dictonary import flatten
from tracardi.service.merging.new.field_merger import FieldMerger

from tracardi.service.setup.mappings.objects.profile import default_profile_properties


def split_flat_profile_to_data_and_timestamps(profile: Dotty) -> Tuple[Dotty, Dict[str, datetime]]:
    profile = profile.copy()
    timestamps = {field: item[0] for field, item in profile.get('metadata.fields', {}).items()}
    del profile['metadata.fields']
    return profile, timestamps


def yield_profiles_and_timestamps(profiles: List[Dotty]):
    for profile in profiles:
        yield split_flat_profile_to_data_and_timestamps(profile)


def _get_profile_fields(profile: Dotty):
    fields = flatten(profile.to_dict()).keys()
    for default_field in default_profile_properties:
        if default_field.property in fields:
            yield default_field.property
        else:
            for f in fields:
                if f.startswith(default_field.property):
                    yield default_field.property


def get_profile_fields(profile: Dotty) -> Set[str]:
    return set(_get_profile_fields(profile))

class FieldManager:

    def __init__(self):
        self.field_settings_by_field = {field.property: field for field in default_profile_properties}

    @staticmethod
    def get_fields(profiles):
        for number, (profile, timestamps) in enumerate(yield_profiles_and_timestamps(profiles)):
            for field in get_profile_fields(profile):
                timestamp = timestamps.get(field, None)
                yield profile, field, profile[field], timestamp

    def get_fields_to_merge(self, profiles):
        properties_to_merge = defaultdict(list)
        field_types = dict()
        field_mergers = dict()
        # Should return profile as well
        for profile, field, value, timestamp in self.get_fields(profiles):

            properties_to_merge[field].append((value, timestamp))

            # Gather field types
            field_setting = self.field_settings_by_field[field]

            field_types[field] = field_setting.type
            field_mergers[field] = field_setting.merge_strategies

        for field, values in properties_to_merge.items():
            yield FieldMerger(
                field=field,
                values=values,
                type=field_types.get(field, None),
                strategies=field_mergers.get(field, None)
            )



