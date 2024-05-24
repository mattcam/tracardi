from typing import List, Tuple, Dict, Set, Generator, Any, Optional

from datetime import datetime
from dotty_dict import Dotty

from tracardi.domain.system_entity_property import SystemEntityProperty
from tracardi.exceptions.log_handler import get_logger
from tracardi.process_engine.tql.utils.dictonary import flatten
from tracardi.service.merging.new.field_metadata import FieldMetaData
from tracardi.service.merging.new.profile_metadata import ProfileMetaData
from tracardi.service.merging.new.value_timestamp import ValueTimestamp

logger = get_logger(__name__)

def split_flat_profile_to_data_and_timestamps(profile: Dotty) -> Tuple[Dotty, Dict[str, datetime]]:
    profile = profile.copy()
    timestamps = {field: item[0] for field, item in profile.get('metadata.fields', {}).items()}
    del profile['metadata.fields']
    return profile, timestamps


# def yield_profiles_and_timestamps(profiles: List[Dotty]):
#     for profile in profiles:
#         yield split_flat_profile_to_data_and_timestamps(profile)


class FieldManager:

    def __init__(self, profiles: List[Dotty]):
        self._profiles = profiles

    @staticmethod
    def _get_profile_fields(properties_settings: List[SystemEntityProperty], profile: Dotty):
        fields = flatten(profile.to_dict()).keys()
        for default_field in properties_settings:
            if default_field.property in fields:
                yield default_field.property
            else:
                for f in fields:
                    if f.startswith(default_field.property):
                        yield default_field.property

    def get_profile_fields(self, properties_settings: List[SystemEntityProperty], profile: Dotty) -> Set[str]:
        return set(self._get_profile_fields(properties_settings, profile))

    def get_profiles_metadata(self, properties_settings: List[SystemEntityProperty], path) -> Generator[ProfileMetaData, Any, Any]:

        field_settings_by_field: Dict[str, SystemEntityProperty] = {field.property: field for field in
                                                                    properties_settings if field.path == path}

        for profile in self._profiles:
            profile, timestamps = split_flat_profile_to_data_and_timestamps(profile)

            properties_to_merge: List[FieldMetaData] = []
            for field in self.get_profile_fields(properties_settings, profile):

                field_setting = field_settings_by_field.get(field, None)
                if not field_setting:
                    raise ValueError(f"No entity setting for field {field}.")

                properties_to_merge.append(
                    FieldMetaData(
                        type=field_setting.type,
                        path=field_setting.path,
                        field=field,
                        values=[ValueTimestamp(
                            value=profile.get(field),
                            timestamp=timestamps.get(field, None),
                            profile_update=profile.get('metadata.time.update', None),
                            profile_insert=profile.get('metadata.time.insert', None)
                        ) for profile in self._profiles],
                        strategies=field_setting.merge_strategies
                    )
                )

            yield ProfileMetaData(
                profile=profile,
                fields_metadata=properties_to_merge
            )
