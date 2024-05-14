from tracardi.context import get_context
from tracardi.domain.system_entity_table_column import SystemEntityTableColumn
from tracardi.service.storage.mysql.schema.table import SystemEntityTableColumnTable

def map_to_system_entity_table_column_table(column: SystemEntityTableColumn) -> SystemEntityTableColumnTable:
    context = get_context()
    return SystemEntityTableColumnTable(
        id=column.id,
        database=column.database,
        table=column.table,
        column=column.column,
        type=column.type,
        default=column.default,  # Properly handles None if default is not set
        nullable=column.nullable,
        tenant=context.tenant
    )

def map_to_system_entity_table_column(column_table: SystemEntityTableColumnTable) -> SystemEntityTableColumn:
    return SystemEntityTableColumn(
        id=column_table.id,
        database=column_table.database,
        table=column_table.table,
        column=column_table.column,
        type=column_table.type,
        default=column_table.default,  # Returns None if default is not set in the table
        nullable=column_table.nullable
    )
