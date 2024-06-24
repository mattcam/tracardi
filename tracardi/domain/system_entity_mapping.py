from tracardi.domain.entity import Entity


class SystemEntityPropertyToColumn(Entity):
    id: str  # e.g. tracardi_profiles
    property_id: str  # profile.id
    column_id: str  # profile_id
    mode: str  # "production",
