from typing import Optional

from datetime import datetime
from tracardi.service.merging.new.value_timestamp import ValueTimestamp


def _convert(field_ref: ValueTimestamp) -> Optional[ValueTimestamp]:
    if field_ref:
        if isinstance(field_ref.timestamp, datetime):
            return ValueTimestamp(field_ref.value, field_ref.timestamp.timestamp())
        return field_ref
    return None
