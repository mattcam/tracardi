from typing import Optional, List

from tracardi.domain.entity import Entity
from tracardi.service.merging.new.merging_strategy_types import LAST_UPDATE, LAST_PROFILE_UPDATE_TIME, \
    LAST_PROFILE_INSERT_TIME


class SystemEntityProperty(Entity):
    entity: str
    path: Optional[str] = None
    property: str
    type: str
    default: Optional[str] = None
    optional: bool = False
    converter: Optional[str] = None
    merge_strategies: Optional[List[str]] = [LAST_UPDATE, LAST_PROFILE_UPDATE_TIME, LAST_PROFILE_INSERT_TIME]
