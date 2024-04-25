from typing import Optional

from tracardi.domain.entity import Entity


class SystemEntityProperty(Entity):
    entity: str
    type: str
    default: Optional[str] = None
    optional: bool = False
    converter: Optional[str] = None
