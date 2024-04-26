from tracardi.domain.entity import Entity


class SystemEntityPropertyToColumn(Entity):
    database: str  # e.g. tracardi_profiles
    table: str # e.g. profile
    column:str # string
    entity: str
    property: str
