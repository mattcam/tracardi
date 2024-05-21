from collections import defaultdict
from typing import List, Any, Tuple, Dict, Set, Optional

from pprint import pprint

from datetime import datetime

import asyncio
from dotty_dict import Dotty
from pydantic import BaseModel

from tracardi.domain.profile import ConsentRevoke
from tracardi.process_engine.tql.utils.dictonary import flatten
from tracardi.service.setup.mappings.objects.profile import default_profile_properties


class FieldMerger(BaseModel):
    field: str
    values: List[Tuple[Any, Optional[datetime]]]
    type: str
    strategy: str

class FieldManager:

    def __init__(self):
        self.field_settings_by_field = {field.property: field for field in default_profile_properties}

    def get_fields(self,profiles):
        for number, (profile, timestamps) in enumerate(yield_profiles_and_timestamps(profiles)):
            for field in get_profile_fields(profile):
                timestamp = timestamps.get(field, None)
                yield number, field, profile[field], timestamp

    def get_fields_to_merge(self, profiles):
        properties_to_merge = defaultdict(list)
        field_types = dict()
        field_mergers = dict()
        for number, field, value, timestamp in self.get_fields(profiles):

            properties_to_merge[field].append((value, timestamp))

            # Gather field types
            field_setting = self.field_settings_by_field[field]

            field_types[field] = field_setting.type
            field_mergers[field] = field_setting.merge_strategy


        result = {}
        for field, values in properties_to_merge.items():
            result[field] = FieldMerger(
                field=field,
                values=values,
                type=field_types.get(field, None),
                strategy=field_mergers.get(field, None)
            )
        pprint(result)
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

async def main():

    profile1 = Dotty({
        'id': 1,
        "metadata": {
            "time": {
                "insert": "2024-05-18T17:13:28.620880+00:00",
                "create": "2024-05-18T17:13:28.620880+00:00",
                "update": "2024-05-20T10:53:41.924819+00:00",
                "segmentation": None,
                "visit": {
                    "last": "2024-05-18T17:13:28.655439+00:00",
                    "current": "2024-05-20T10:23:52.968274+00:00",
                    "count": 2,
                    "tz": "Europe/Warsaw"
                }
            },
            "aux": {},
            "status": None,
            "fields": {
                "traits.a": [
                    "2024-05-20 10:53:41.923018+00:00",
                    "19fc6fa0-11f1-4737-bb33-d8e140ee54b2"
                ],
                "consents.marketing": [
                    "2024-05-20 10:53:41.923037+00:00",
                    "19fc6fa0-11f1-4737-bb33-d8e140ee54b2"
                ],
                "consents.ident": [
                    "2024-05-20 10:53:41.923044+00:00",
                    "19fc6fa0-11f1-4737-bb33-d8e140ee54b2"
                ],
                "aux.isProfessionalQuestion": [
                    "2024-05-20 10:53:41.923050+00:00",
                    "19fc6fa0-11f1-4737-bb33-d8e140ee54b2"
                ],
                "metadata.time.visit.tz": [
                    "2024-05-21 13:33:41.923050+00:00",
                    "19fc6fa0-11f1-4737-bb33-d8e140ee54b2"
                ],
            },
            "system": {
                "integrations": {},
                "aux": {
                    "a": 1
                }
            }
        },
        'traits': {
          "a": 1
        },
        'consents': {
            'marketing': ConsentRevoke(revoke=None),
            'ident': ConsentRevoke(revoke=datetime.now())
        },
    })

    profile2 = Dotty({
        'id': 1,
        "metadata": {
            "time": {
                "insert": "2024-05-18T17:13:28.620880+00:00",
                "create": "2024-05-18T17:13:28.620880+00:00",
                "update": "2024-05-20T10:53:41.924819+00:00",
                "segmentation": None,
                "visit": {
                    "last": "2024-05-18T17:13:28.655439+00:00",
                    "current": "2024-05-20T10:23:52.968274+00:00",
                    "count": 2,
                    "tz": "Europe/Berlin"
                }
            },
            "aux": {},
            "status": None,
            "fields": {
                "traits.a": [
                    "2024-05-20 10:53:41.923018+00:00",
                    "19fc6fa0-11f1-4737-bb33-d8e140ee54b2"
                ],
                "traits.b": [
                    "2024-05-20 10:53:41.923018+00:00",
                    "19fc6fa0-11f1-4737-bb33-d8e140ee54b2"
                ],
                "consent.marketing": [
                    "2024-05-20 11:53:41.923037+00:00",
                    "19fc6fa0-11f1-4737-bb33-d8e140ee54b2"
                ],
                "consent.ident": [
                    "2024-05-20 11:53:41.923044+00:00",
                    "19fc6fa0-11f1-4737-bb33-d8e140ee54b2"
                ],
                "consent.email": [
                    "2024-05-20 11:53:42.923050+00:00",
                    "19fc6fa0-11f1-4737-bb33-d8e140ee54b2"
                ]
            },
            "system": {
                "integrations": {},
                "aux": {
                    "a": 1
                }
            }
        },
        'traits': {
            "a": 2,
            "b": 1
        },
        'consents': {
            'marketing': ConsentRevoke(revoke=datetime.now()),
            'ident': ConsentRevoke(revoke=datetime.now()),
            'email': ConsentRevoke(revoke=None),
        }
    })

    profile3 = Dotty({
        'id': 1,
        "metadata": {
            "time": {
                "insert": "2024-05-18T17:13:28.620880+00:00",
                "create": "2024-05-18T17:13:28.620880+00:00",
                "update": "2024-05-20T10:53:41.924819+00:00",
                "segmentation": None,
                "visit": {
                    "last": "2024-05-18T17:13:28.655439+00:00",
                    "current": "2024-05-20T10:23:52.968274+00:00",
                    "count": 2,
                    "tz": "Europe/Berlin"
                }
            },
            "aux": {},
            "status": None,
            "fields": {
                "traits.a": [
                    "2024-05-20 12:53:41.923018+00:00",
                    "19fc6fa0-11f1-4737-bb33-d8e140ee54b2"
                ],
                "traits.c": [
                    "2024-05-20 12:53:41.923018+00:00",
                    "19fc6fa0-11f1-4737-bb33-d8e140ee54b2"
                ],
                "system.aux.a": [
                    "2024-05-20 12:53:41.923018+00:00",
                    "19fc6fa0-11f1-4737-bb33-d8e140ee54b2"
                ]
            },
            "system": {
                "integrations": {},
                "aux": {
                    "a": 1
                }
            }
        },
        'traits': {
            "a": 2,
            "c": 1
        }
    })

    profiles = [profile1, profile2, profile3]

    fm = FieldManager()
    fm.get_fields_to_merge(profiles)


asyncio.run(main())