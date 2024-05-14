from tracardi.domain.system_entity_table_column import SystemEntityTableColumn


default_session_table_columns = [
    SystemEntityTableColumn(
        id="c1e40a5d-2116-4d9c-b160-7d5c99dec9f6",
        database="tracardi",
        table="session",
        column="id",
        type="string",
        default=None,
        nullable=False
    ),
]


# from uuid import uuid4
# from tracardi.service.setup.mappings.objects.session import default_session_properties
#
#
# db = {v.property.replace(".", "_"):v.id for v in default_session_properties}
#
# for x in default_session_table_columns:
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