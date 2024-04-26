from tracardi.domain.system_entity_mapping import SystemEntityPropertyToColumn
from tracardi.domain.system_entity_table_column import SystemEntityTableColumn

default_event_table_columns = [
    SystemEntityTableColumn(
        id="id",
        database="tracardi",
        table="event",
        type="string",
        default=None,
        nullable=False
    ),
]
event_properties_to_column_mapping = [
    SystemEntityPropertyToColumn(
        id="715b3759-2328-4e92-a15a-68eaf3f937af",
        database="tracardi",
        table="event",
        column="id",
        entity="event",
        entity_property="id"
    ),
]