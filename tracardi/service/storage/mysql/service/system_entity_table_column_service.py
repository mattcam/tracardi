from typing import Tuple, Optional, List

from tracardi.domain.setting import Setting
from tracardi.domain.system_entity_table_column import SystemEntityTableColumn
from tracardi.exceptions.log_handler import get_logger
from tracardi.service.storage.mysql.mapping.system_entity_table_column_mapping import map_to_system_entity_table_column, \
    map_to_system_entity_table_column_table
from tracardi.service.storage.mysql.schema.table import SystemEntityTableColumnTable
from tracardi.service.storage.mysql.service.table_service import TableService
from tracardi.service.storage.mysql.utils.select_result import SelectResult


logger = get_logger(__name__)

class SystemEntityTableColumnService(TableService):
    async def load_all(self, search: str = None, limit: int = None, offset: int = None) -> SelectResult:
        return await self._load_all_in_deployment_mode(SystemEntityTableColumnTable, search, limit, offset)

    async def load_by_id(self, column_id: str) -> SelectResult:
        return await self._load_by_id_in_deployment_mode(SystemEntityTableColumnTable, primary_id=column_id)

    async def delete_by_id(self, column_id: str) -> Tuple[bool, Optional[Setting]]:
        return await self._delete_by_id_in_deployment_mode(
            SystemEntityTableColumnTable,
            map_to_system_entity_table_column,
            primary_id=column_id)

    async def insert(self, default_entity_column: SystemEntityTableColumn):
        return await self._replace(
            SystemEntityTableColumnTable,
            map_to_system_entity_table_column_table(default_entity_column))

    @staticmethod
    async def bootstrap(default_entity_columns: List[SystemEntityTableColumn]):
        service = SystemEntityTableColumnService()
        for column in default_entity_columns:
            await service.insert(column)
            logger.info(f"System table column {column.database}.{column.table}.{column.id} installed.")
