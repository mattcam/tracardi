from typing import Optional

from tracardi.domain.entity import Entity
from tracardi.domain.merging_strategy import LATEST_UPDATE


class SystemEntityProperty(Entity):
    entity: str
    property: str
    type: str
    default: Optional[str] = None
    optional: bool = False
    converter: Optional[str] = None
    merge_strategy: Optional[str] = LATEST_UPDATE
