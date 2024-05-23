from typing import Optional

from datetime import datetime

from tracardi.service.merging.new.field_ref import FieldRef


def _convert(field_ref: FieldRef) -> Optional[FieldRef]:
    if field_ref:
        if isinstance(field_ref.timestamp, datetime):
            return FieldRef(field_ref.profile, field_ref.field, field_ref.value, field_ref.timestamp.timestamp())
        return field_ref
    return None
