from typing import List

from tracardi.domain.system_entity_mapping import SystemEntityPropertyToColumn
from tracardi.exceptions.log_handler import get_logger
from tracardi.service.storage.mysql.mapping.system_entity_property_to_column_mapping import \
    map_to_system_entity_property_to_column_table
from tracardi.service.storage.mysql.schema.table import SystemEntityPropertyToColumnMappingTable
from tracardi.service.storage.mysql.service.table_service import TableService

logger = get_logger(__name__)

class SystemEntityPropertyToColumnMapping(TableService):


    async def insert(self, mapping: SystemEntityPropertyToColumn):
        return await self._replace(
            SystemEntityPropertyToColumnMappingTable,
            map_to_system_entity_property_to_column_table(mapping))

    @staticmethod
    async def bootstrap(default_mappings: List[SystemEntityPropertyToColumn]):
        service = SystemEntityPropertyToColumnMapping()
        for mapping in default_mappings:
            await service.insert(mapping)
            logger.info(f"Table column {mapping.column_id} mapped to {mapping.property_id}.")