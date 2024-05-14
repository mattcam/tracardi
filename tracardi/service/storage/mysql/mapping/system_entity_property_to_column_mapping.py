from tracardi.context import get_context
from tracardi.domain.system_entity_mapping import SystemEntityPropertyToColumn
from tracardi.service.storage.mysql.schema.table import SystemEntityPropertyToColumnMappingTable


def map_to_system_entity_property_to_column_table(mapping: SystemEntityPropertyToColumn) -> SystemEntityPropertyToColumnMappingTable:
    context = get_context()
    return SystemEntityPropertyToColumnMappingTable(
        id=mapping.id,
        property_id=mapping.property_id,
        column_id=mapping.column_id,
        mode=mapping.mode,
        tenant=context.tenant
    )

def map_to_system_entity_property_to_column(mapping_table: SystemEntityPropertyToColumnMappingTable) -> SystemEntityPropertyToColumn:
    return SystemEntityPropertyToColumn(
        id=mapping_table.id,
        property_id=mapping_table.property_id,
        column_id=mapping_table.column_id,
        mode=mapping_table.mode
    )
