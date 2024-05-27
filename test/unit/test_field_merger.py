from dotty_dict import Dotty

from tracardi.service.merging.new.field_manager import FieldManager, ProfileDataSpliter
from tracardi.service.merging.new.merging_strategy_types import DEFAULT_STRATEGIES
from tracardi.service.setup.mappings.objects.profile import default_profile_properties


def test_field_merger():
    profile1 = Dotty({
        'id': 1,
        'active': True,
        "data": {"anonymous": "TRUE", "pii": {"language": {"spoken": ['polish']}}},
        'traits': {
            "a": 1
        },
        "metadata": {
            "fields": {
                "data.anonymous": [
                    "2024-05-20 12:53:41.923018+00:00",
                    "19fc6fa0-11f1-4737-bb33-d8e140ee54b2"
                ]
            },
        }
    })

    profile2 = Dotty({
        'id': 2,
        'active': False,
        'traits': {
            "a": 2,
            "b": 1
        },
        "data": {"anonymous": "TRUE", "preferences": {"payments": []}},
        "metadata": {
            "fields": {
                "data.anonymous": [
                    "2020-05-20 12:53:41.923018+00:00",
                    "19fc6fa0-11f1-4737-bb33-d8e140ee54b2"
                ]
            },
        }
    })

    profiles = [profile1, profile2]

    indexed_properties_settings = {field.property: field for field in default_profile_properties if field.path == ""}

    fm = ProfileDataSpliter(profiles)
    props, timestamps = fm._get_fields_and_timestamps(indexed_properties_settings, default_strategies=[])
    props = {x.property for x in props}
    assert props == {'active', 'data.pii.language.spoken', 'data.anonymous', 'traits', 'id',
                     'data.preferences.payments'}
    assert list(timestamps[1].field.values()) == [{'data.anonymous': '2024-05-20 12:53:41.923018+00:00'},{'data.anonymous': '2020-05-20 12:53:41.923018+00:00'}]

    result = fm.get_profiles_metadata(default_profile_properties,path="", default_strategies=DEFAULT_STRATEGIES)
    result = result.filter('data.anonymous')
    assert result[0].values[0].timestamp.year == 2024
    assert result[0].values[1].timestamp.year == 2020