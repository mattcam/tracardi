from tracardi.domain.system_entity_mapping import SystemEntityPropertyToColumn
from tracardi.domain.system_entity_table_column import SystemEntityTableColumn

default_session_table_columns = [
    SystemEntityTableColumn(
        id="c1e40a5d-2116-4d9c-b160-7d5c99dec9f6",
        database="tracardi",
        table="session",
        column="id",
        type="string",
        default=None,
        nullable=False
    ),
]

session_properties_to_column_mapping = [
    SystemEntityPropertyToColumn(
        id="ceea19fe-b1d1-44f8-9838-4ca9ffb8f690",
        database="tracardi",
        table="session",
        column="id",
        entity="session",
        entity_property="id"
    ),
]