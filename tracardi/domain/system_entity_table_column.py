from typing import Optional

from tracardi.domain.entity import Entity


class SystemEntityTableColumn(Entity):
    database: str  # e.g. tracardi_profiles
    table: str # e.g. profile
    column: str
    type:str # string
    default: Optional[str] = None
    nullable: Optional[bool] = False