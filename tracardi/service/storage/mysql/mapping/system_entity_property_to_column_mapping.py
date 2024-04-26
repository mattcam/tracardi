from tracardi.context import get_context
from tracardi.domain.system_entity_mapping import SystemEntityPropertyToColumn
from tracardi.service.storage.mysql.schema.table import SystemEntityPropertyToColumnMappingTable


def map_to_system_entity_property_to_column_table(mapping: SystemEntityPropertyToColumn) -> SystemEntityPropertyToColumnMappingTable:
    context = get_context()
    return SystemEntityPropertyToColumnMappingTable(
        id=mapping.id,
        database=mapping.database,
        table=mapping.table,
        column=mapping.column,
        entity=mapping.entity,  # Properly handles None if default is not set
        entity_property=mapping.entity_property,
        tenant=context.tenant,
        production=context.production
    )

def map_to_system_entity_property_to_column(mapping_table: SystemEntityPropertyToColumnMappingTable) -> SystemEntityPropertyToColumn:
    return SystemEntityPropertyToColumn(
        id=mapping_table.id,
        database=mapping_table.database,
        table=mapping_table.table,
        column=mapping_table.type,
        entity=mapping_table.entity,
        entity_property=mapping_table.entity_property
    )
