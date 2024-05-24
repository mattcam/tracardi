from datetime import datetime
from typing import Any, Union, Optional
from pydantic import BaseModel


class ValueTimestamp(BaseModel):
    value: Any
    timestamp: Optional[Union[datetime, float]] = None
    profile_update: Optional[Union[datetime, float, str]] = None
    profile_insert: Optional[Union[datetime, float, str]] = None
