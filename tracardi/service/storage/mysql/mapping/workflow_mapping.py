from tracardi.context import get_context
from tracardi.domain.flow import FlowRecord
from tracardi.domain.flow_meta_data import FlowMetaData
from tracardi.service.storage.mysql.mapping.utils import split_list
from tracardi.service.storage.mysql.schema.table import WorkflowTable


def map_to_workflow_table(flow_record: FlowRecord) -> WorkflowTable:

    context = get_context()

    return WorkflowTable(
        id=flow_record.id,
        timestamp=flow_record.timestamp,
        deploy_timestamp=flow_record.deploy_timestamp,
        name=flow_record.name,
        description=flow_record.description,
        type=flow_record.type,
        projects=",".join(flow_record.projects) if flow_record.projects else "",

        draft=flow_record.draft.encode(),

        lock=flow_record.lock,

        tenant = context.tenant,
        production = context.production

    )

# Mapping from SQLAlchemy Table to Domain Object
def map_to_workflow_record(workflow_table: WorkflowTable) -> FlowRecord:
    return FlowRecord(
        id=workflow_table.id,
        timestamp=workflow_table.timestamp,
        deploy_timestamp=workflow_table.deploy_timestamp,
        name=workflow_table.name,
        description=workflow_table.description,
        type=workflow_table.type,
        projects=split_list(workflow_table.projects),
        draft=workflow_table.draft.decode(),
        lock=workflow_table.lock,
        running=workflow_table.running
    )


def map_to_workflow_record_meta(workflow_table: WorkflowTable) -> FlowMetaData:
    return FlowMetaData(
        id=workflow_table.id,
        name=workflow_table.name,
        description=workflow_table.description,
        type=workflow_table.type,
        projects=split_list(workflow_table.projects),

        production=workflow_table.production,
        running=workflow_table.running
    )
