from datetime import datetime


def _convert(field_data):
    if field_data:
        field, timestamp = field_data
        if isinstance(timestamp, datetime):
            return field, timestamp.timestamp()
        return field, timestamp
    return None
