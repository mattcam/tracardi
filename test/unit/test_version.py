from tracardi.domain.version import Version


def test_version_name():
    version = Version(version="0.9.1-dev", db_version="091x")
    assert version.name == Version._generate_name("091x")
