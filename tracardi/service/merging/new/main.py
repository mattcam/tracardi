import time

from datetime import datetime

import asyncio
from dotty_dict import Dotty


from tracardi.domain.profile import ConsentRevoke
from tracardi.service.merging.new.field_manager import FieldManager


async def main():

    profile1 = Dotty({
        'id': 1,
        'active': True,
        "metadata": {
            "time": {
                "insert": "2004-01-18T17:13:28.620880+00:00",
                "create": "2004-01-18T17:13:28.620880+00:00",
                "update": "2004-03-20T10:53:41.924819+00:00",
                "segmentation": None,
                "visit": {
                    "last": "2023-03-18T17:13:28.655439+00:00",
                    "current": "2024-01-20T10:23:52.968274+00:00",
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
        "data": {"anonymous": "TRUE", "pii": {"language": {"spoken": ['polish']}}},
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
        'active': False,
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
        'active': True,
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
        "data": {"anonymous": "TRUE", "pii": {"language": {"spoken": ['english', 'polish']}}},
        'traits': {
            "a": 2,
            "c": 1
        }
    })

    profiles = [profile1, profile2, profile3]

    fm = FieldManager()
    for field in fm.get_fields_to_merge(profiles):
        print(field)
        try:
            merged_value = field.merge()
            print(merged_value)
            print(field.field, merged_value.value, time.time())

        except ValueError as e:
            print("Cant", str(e))
        print('---------')


asyncio.run(main())