from typing import Protocol, List, Tuple, Any, Union, Optional
from datetime import datetime

from tracardi.service.merging.new.field_ref import FieldRef


class StrategyProtocol(Protocol):
    def prerequisites(self) -> bool:
        ...

    def merge(self) -> FieldRef:
        ...