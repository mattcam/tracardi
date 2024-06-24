from dotty_dict import Dotty

from tracardi.service.merging.new.field_manager import FieldManager, ProfileDataSpliter, ProfileTimestamps
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

    fm = ProfileDataSpliter(profiles, indexed_properties_settings, path="", default_strategies=DEFAULT_STRATEGIES, skip_values=[])
    props, timestamps = fm.split()
    props = {x.property for x in props}
    assert props == {'active', 'data.pii.language.spoken', 'data.anonymous', 'traits', 'id',
                     'data.preferences.payments'}

    assert timestamps['1'] == ProfileTimestamps(insert=None, update=None, field={'data.anonymous': '2024-05-20 12:53:41.923018+00:00'})
    assert timestamps['2'] == ProfileTimestamps(insert=None, update=None, field={'data.anonymous': '2020-05-20 12:53:41.923018+00:00'})

    fields, timestamps = fm.split()
    print(timestamps)
    # result = result.filter('data.anonymous')
    # assert result[0].values[0].timestamp.year == 2024
    # assert result[0].values[1].timestamp.year == 2020