from tracardi.domain.system_entity_table_column import SystemEntityTableColumn


default_event_table_columns = [
    SystemEntityTableColumn(
        id="ff7d73f3-4310-4e4f-ae93-59d2ac731d95",
        database="tracardi",
        table="event",
        column="id",
        type="string",
        default=None,
        nullable=False
    ),
]


# from uuid import uuid4
# from tracardi.service.setup.mappings.objects.event import default_event_properties
# db = {v.property.replace(".", "_"):v.id for v in default_event_properties}
#
# for x in default_event_table_columns:
#     print(
# f"""SystemEntityPropertyToColumn(
#     id = "{uuid4()}",
#     property_id = "{db.get(x.column)}",  # {x.column.replace("_", ".")}
#     column_id = "{x.id}",  # {x.column}
#     mode = "production",
#     tenant="default"
# ),"""
#     )
#     print(
#         f"""SystemEntityPropertyToColumn(
#         id = "{uuid4()}",
#         property_id = "{db.get(x.column)}",  # {x.column.replace("_", ".")}
#         column_id = "{x.id}",  # {x.column}
#         mode = "test",
#         tenant="default"
#     ),"""
#     )