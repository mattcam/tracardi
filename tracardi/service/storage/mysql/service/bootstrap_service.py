from tracardi.service.license import License, LICENSE
from tracardi.service.setup.mappings.objects.profile import default_profile_properties
from tracardi.service.setup.mappings.tables.profile import default_profile_table_columns
from tracardi.service.storage.mysql.bootstrap.bridge import os_default_bridges
from tracardi.service.storage.mysql.service.bridge_service import BridgeService
from tracardi.service.storage.mysql.service.system_entity_properties_service import SystemEntityPropertiesService
from tracardi.service.storage.mysql.service.system_entity_table_column_service import SystemEntityTableColumnService

if License.has_license():
    from com_tracardi.db.bootstrap.default_bridges import commercial_default_bridges


async def bootstrap_table_content():
    await BridgeService.bootstrap(default_bridges=os_default_bridges)
    if License.has_service(LICENSE):
        await BridgeService.bootstrap(default_bridges=commercial_default_bridges)

    # Default object properties
    await SystemEntityPropertiesService.bootstrap(default_profile_properties)

    # Default object storage columns
    await SystemEntityTableColumnService.bootstrap(default_profile_table_columns)
