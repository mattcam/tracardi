from collections import namedtuple
from uuid import uuid4

from typing import List, Tuple, Dict, Set

from datetime import datetime
from dotty_dict import Dotty

from tracardi.domain.system_entity_property import SystemEntityProperty
from tracardi.exceptions.log_handler import get_logger
from tracardi.process_engine.tql.utils.dictonary import flatten
from tracardi.service.merging.new.field_metadata import FieldMetaData
from tracardi.service.merging.new.merging_strategy_types import LAST_UPDATE, LAST_PROFILE_UPDATE_TIME, \
    LAST_PROFILE_INSERT_TIME
from tracardi.service.merging.new.profile_metadata import ProfileMetaData
from tracardi.service.merging.new.value_timestamp import ValueTimestamp

logger = get_logger(__name__)

ValueAndTimestamp = namedtuple('ValueAndTimestamp', ['profile', 'value', 'timestamp'])

def split_flat_profile_to_data_and_timestamps(profile: Dotty) -> Tuple[Dotty, Dict[str, datetime]]:
    profile = profile.copy()
    timestamps = {field: item[0] for field, item in profile.get('metadata.fields', {}).items()}
    return profile, timestamps




class FieldManager:

    def __init__(self, profiles: List[Dotty]):
        self._profiles = profiles

    @staticmethod
    def _get_profile_fields(properties_settings: List[SystemEntityProperty], profile: Dotty, path):
        fields = flatten(profile.to_dict()).keys()

        # TODO odwrocic iteracje aby dostac tez nie zmappowane pola.

        for default_field in properties_settings:

            # Skip all with wrong path.Path filtering
            if not default_field.path.startswith(path):
                continue

            if default_field.property in fields:
                yield default_field.property
            else:
                for f in fields:
                    if f.startswith(default_field.property):
                        yield default_field.property

    def get_profile_fields(self, properties_settings: List[SystemEntityProperty], profile: Dotty, path: str = "") -> Set[str]:
        # Skip timestamp fields
        return {item for item in self._get_profile_fields(properties_settings, profile, path) if not item.startswith('metadata.fields')}

    def _get_fields_and_timestamps(self, properties_settings, path: str ="") -> Tuple[Set[str], Dict[str, Dict[str, datetime]]]:
        set_of_fields = set()
        profile_id_to_timestamps = {}
        for profile in self._profiles:
            profile, timestamps = split_flat_profile_to_data_and_timestamps(profile)
            profile_id_to_timestamps[profile['id']] = timestamps
            for field in self.get_profile_fields(properties_settings, profile, path):
                set_of_fields.add(field)
        return set_of_fields, profile_id_to_timestamps

    def get_profiles_metadata(self, properties_settings: List[SystemEntityProperty], path) -> ProfileMetaData:

        field_settings_by_field: Dict[str, SystemEntityProperty] = {field.property: field for field in
                                                                    properties_settings if field.path == path}
        print('field mapping', field_settings_by_field.keys())
        combined_profile_fields, profile_id_to_timestamps = self._get_fields_and_timestamps(properties_settings, path)
        print('all fields intersected with field mapping', combined_profile_fields)

        properties_to_merge: List[FieldMetaData] = []
        for field in combined_profile_fields:
            field_setting = field_settings_by_field.get(field, None)
            if not field_setting:
                # Default setting for not defined mapping
                field_setting = SystemEntityProperty(
                    id=str(uuid4()),
                    entity='profile',
                    property=field,
                    type='unknown',
                    merge_strategies=[LAST_UPDATE, LAST_PROFILE_UPDATE_TIME, LAST_PROFILE_INSERT_TIME]
                )
                # raise ValueError(f"No entity setting for field {field}.")

            properties_to_merge.append(
                FieldMetaData(
                    type=field_setting.type,
                    path=field_setting.path,
                    field=field,
                    values=[ValueTimestamp(
                        value=profile.get(field),
                        timestamp=profile_id_to_timestamps.get(profile['id'], {}).get(field, None),
                        profile_update=profile.get('metadata.time.update', None),
                        profile_insert=profile.get('metadata.time.insert', None)
                    ) for profile in self._profiles],
                    strategies=field_setting.merge_strategies
                )
            )

        return ProfileMetaData(
            profiles=self._profiles,
            fields_metadata=properties_to_merge
        )

