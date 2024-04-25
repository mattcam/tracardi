from typing import Tuple, Optional, List

from tracardi.domain.setting import Setting
from tracardi.domain.system_entity_property import SystemEntityProperty
from tracardi.exceptions.log_handler import get_logger
from tracardi.service.storage.mysql.mapping.system_entity_property_mapping import map_to_system_entity_property, \
    map_to_system_entity_property_table
from tracardi.service.storage.mysql.schema.table import SystemEntityPropertyTable
from tracardi.service.storage.mysql.service.table_service import TableService
from tracardi.service.storage.mysql.utils.select_result import SelectResult


logger = get_logger(__name__)

class SystemEntityPropertiesService(TableService):
    async def load_all(self, search: str = None, limit: int = None, offset: int = None) -> SelectResult:
        return await self._load_all_in_deployment_mode(SystemEntityPropertyTable, search, limit, offset)

    async def load_by_id(self, field_id: str) -> SelectResult:
        return await self._load_by_id_in_deployment_mode(SystemEntityPropertyTable, primary_id=field_id)

    async def delete_by_id(self, field_id: str) -> Tuple[bool, Optional[Setting]]:
        return await self._delete_by_id_in_deployment_mode(
            SystemEntityPropertyTable,
            map_to_system_entity_property,
            primary_id=field_id)

    async def insert(self, system_entity_property: SystemEntityProperty):
        return await self._replace(
            SystemEntityPropertyTable,
            map_to_system_entity_property_table(system_entity_property))

    @staticmethod
    async def bootstrap(default_system_entity_properties: List[SystemEntityProperty]):
        seps = SystemEntityPropertiesService()
        for property in default_system_entity_properties:
            await seps.insert(property)
            logger.info(f"System property {property.id} installed.")
