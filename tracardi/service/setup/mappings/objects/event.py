event_properties = [
    {
        "field": "id",
        "type": "str",
        "optional": False,
        "default": None
    },
    {
        "field": "metadata.aux",
        "type": "dict",
        "optional": True,
        "default": "{}"
    },
    {
        "field": "metadata.time.insert",
        "type": "datetime",
        "optional": True,
        "default": "NULL"
    },
    {
        "field": "metadata.time.create",
        "type": "datetime",
        "optional": True,
        "default": "NULL"
    },
    {
        "field": "metadata.time.update",
        "type": "datetime",
        "optional": True,
        "default": "NULL"
    },
    {
        "field": "metadata.time.process_time",
        "type": "float",
        "optional": True,
        "default": "0"
    },
    {
        "field": "metadata.time.total_time",
        "type": "float",
        "optional": True,
        "default": "0"
    },
    {
        "field": "metadata.ip",
        "type": "str",
        "optional": True,
        "default": "NULL"
    },
    {
        "field": "metadata.status",
        "type": "str",
        "optional": True,
        "default": "'collected'"
    },
    {
        "field": "metadata.channel",
        "type": "str",
        "optional": True,
        "default": "NULL"
    },
    {
        "field": "metadata.processed_by.rules",
        "type": "List[str]",
        "optional": False,
        "default": "[]"
    },
    {
        "field": "metadata.processed_by.flows",
        "type": "List[str]",
        "optional": False,
        "default": "[]"
    },
    {
        "field": "metadata.processed_by.third_party",
        "type": "List[str]",
        "optional": False,
        "default": "[]"
    },
    {
        "field": "metadata.profile_less",
        "type": "bool",
        "optional": True,
        "default": "False"
    },
    {
        "field": "metadata.debug",
        "type": "bool",
        "optional": True,
        "default": "False"
    },
    {
        "field": "metadata.valid",
        "type": "bool",
        "optional": True,
        "default": "True"
    },
    {
        "field": "metadata.error",
        "type": "bool",
        "optional": True,
        "default": "False"
    },
    {
        "field": "metadata.warning",
        "type": "bool",
        "optional": True,
        "default": "False"
    },
    {
        "field": "metadata.merge",
        "type": "bool",
        "optional": True,
        "default": "False"
    },
    {
        "field": "metadata.instance",
        "type": "Entity",
        "optional": True,
        "default": "NULL"
    },
    {
        "field": "session.id",
        "type": "str",
        "optional": False,
        "default": "NULL"
    },
    {
        "field": "session.start",
        "type": "datetime",
        "optional": False,
        "default": "now_in_utc()"
    },
    {
        "field": "session.duration",
        "type": "float",
        "optional": False,
        "default": "0"
    },
    {
        "field": "session.tz",
        "type": "str",
        "optional": True,
        "default": "NULL"
    },
    {
        "field": "profile",
        "type": "PrimaryEntity",
        "optional": True,
        "default": "NULL"
    },
    {
        "field": "context",
        "type": "dict",
        "optional": True,
        "default": "{}"
    },
    {
        "field": "request",
        "type": "dict",
        "optional": True,
        "default": "{}"
    },
    {
        "field": "config",
        "type": "dict",
        "optional": True,
        "default": "{}"
    },
    {
        "field": "tags.values",
        "type": "Tuple[str, ...]",
        "optional": False,
        "default": "()"
    },
    {
        "field": "tags.count",
        "type": "int",
        "optional": False,
        "default": "0"
    },
    {
        "field": "aux",
        "type": "dict",
        "optional": False,
        "default": "{}"
    },
    {
        "field": "device",
        "type": "dict",
        "optional": True,
        "default": "{}"
    },
    {
        "field": "os",
        "type": "dict",
        "optional": True,
        "default": "{}"
    },
    {
        "field": "app",
        "type": "dict",
        "optional": True,
        "default": "{}"
    },
    {
        "field": "hit",
        "type": "dict",
        "optional": True,
        "default": "{}"
    },
    {
        "field": "journey.state",
        "type": "str",
        "optional": True,
        "default": "NULL"
    },
    {
        "field": "data",
        "type": "dict",
        "optional": True,
        "default": "{}"
    },
    {
        "field": "id",
        "type": "str",
        "optional": False,
        "default": "NULL"
    },
    {
        "field": "type",
        "type": "str",
        "optional": False,
        "default": "NULL"
    },
    {
        "field": "name",
        "type": "str",
        "optional": False,
        "default": "capitalize_event_type_id(type)"
    },
    {
        "field": "metadata.aux",
        "type": "dict",
        "optional": True,
        "default": "{}"
    },
    {
        "field": "metadata.time.insert",
        "type": "datetime",
        "optional": True,
        "default": "NULL"
    },
    {
        "field": "metadata.time.create",
        "type": "datetime",
        "optional": True,
        "default": "NULL"
    },
    {
        "field": "metadata.time.update",
        "type": "datetime",
        "optional": True,
        "default": "NULL"
    },
    {
        "field": "metadata.time.process_time",
        "type": "float",
        "optional": True,
        "default": "0"
    },
    {
        "field": "metadata.ip",
        "type": "str",
        "optional": True,
        "default": "NULL"
    },
    {
        "field": "metadata.status",
        "type": "str",
        "optional": True,
        "default": "NULL"
    },
    {
        "field": "metadata.channel",
        "type": "str",
        "optional": True,
        "default": "NULL"
    },
    {
        "field": "metadata.processed_by.rules",
        "type": "List[str]",
        "optional": False,
        "default": "[]"
    },
    {
        "field": "metadata.processed_by.flows",
        "type": "List[str]",
        "optional": False,
        "default": "[]"
    },
    {
        "field": "metadata.processed_by.third_party",
        "type": "List[str]",
        "optional": False,
        "default": "[]"
    },
    {
        "field": "metadata.profile_less",
        "type": "bool",
        "optional": True,
        "default": "False"
    },
    {
        "field": "metadata.debug",
        "type": "bool",
        "optional": True,
        "default": "False"
    },
    {
        "field": "metadata.valid",
        "type": "bool",
        "optional": True,
        "default": "True"
    },
    {
        "field": "metadata.error",
        "type": "bool",
        "optional": True,
        "default": "False"
    },
    {
        "field": "metadata.warning",
        "type": "bool",
        "optional": True,
        "default": "False"
    },
    {
        "field": "metadata.merge",
        "type": "bool",
        "optional": True,
        "default": "False"
    },
    {
        "field": "metadata.instance.id",
        "type": "str",
        "optional": True,
        "default": "NULL"
    },
    {
        "field": "utm.source",
        "type": "str",
        "optional": True,
        "default": "NULL"
    },
    {
        "field": "utm.medium",
        "type": "str",
        "optional": True,
        "default": "NULL"
    },
    {
        "field": "utm.campaign",
        "type": "str",
        "optional": True,
        "default": "NULL"
    },
    {
        "field": "utm.term",
        "type": "str",
        "optional": True,
        "default": "NULL"
    },
    {
        "field": "utm.content",
        "type": "str",
        "optional": True,
        "default": "NULL"
    },
    {
        "field": "operation.new",
        "type": "bool",
        "optional": True,
        "default": "False"
    },
    {
        "field": "operation.update",
        "type": "bool",
        "optional": True,
        "default": "False"
    },
    {
        "field": "source.id",
        "type": "str",
        "optional": True,
        "default": "NULL"
    },
    {
        "field": "source.type",
        "type": "List[str]",
        "optional": True,
        "default": "[]"
    },
    {
        "field": "source.bridge.id",
        "type": "str",
        "optional": True,
        "default": "NULL"
    },
    {
        "field": "source.bridge.name",
        "type": "str",
        "optional": True,
        "default": "NULL"
    },
    {
        "field": "source.timestamp",
        "type": "datetime",
        "optional": True,
        "default": "NULL"
    },
    {
        "field": "source.name",
        "type": "str",
        "optional": True,
        "default": "NULL"
    },
    {
        "field": "source.description",
        "type": "str",
        "optional": True,
        "default": "NULL"
    },
    {
        "field": "source.channel",
        "type": "str",
        "optional": True,
        "default": "NULL"
    },
    {
        "field": "source.enabled",
        "type": "bool",
        "optional": True,
        "default": "True"
    },
    {
        "field": "source.transitional",
        "type": "bool",
        "optional": True,
        "default": "False"
    },
    {
        "field": "source.tags",
        "type": "List[str]",
        "optional": True,
        "default": "[]"
    },
    {
        "field": "source.groups",
        "type": "List[str]",
        "optional": True,
        "default": "[]"
    },
    {
        "field": "source.returns_profile",
        "type": "bool",
        "optional": True,
        "default": "False"
    },
    {
        "field": "source.permanent_profile_id",
        "type": "bool",
        "optional": True,
        "default": "False"
    },
    {
        "field": "source.requires_consent",
        "type": "bool",
        "optional": True,
        "default": "False"
    },
    {
        "field": "source.manual",
        "type": "bool",
        "optional": True,
        "default": "NULL"
    },
    {
        "field": "source.locked",
        "type": "bool",
        "optional": True,
        "default": "False"
    },
    {
        "field": "source.synchronize_profiles",
        "type": "bool",
        "optional": True,
        "default": "True"
    },
    {
        "field": "source.config",
        "type": "dict",
        "optional": True,
        "default": "{}"
    },
    {
        "field": "session.id",
        "type": "str",
        "optional": False,
        "default": "session_id"
    },
    {
        "field": "session.start",
        "type": "datetime",
        "optional": True,
        "default": "NULL"
    },
    {
        "field": "session.duration",
        "type": "float",
        "optional": False,
        "default": "0"
    },
    {
        "field": "session.tz",
        "type": "str",
        "optional": True,
        "default": "'utc'"
    },
    {
        "field": "profile.id",
        "type": "str",
        "optional": True,
        "default": "profile_id"
    },
    {
        "field": "context",
        "type": "dict",
        "optional": True,
        "default": "context"
    },
    {
        "field": "request",
        "type": "dict",
        "optional": True,
        "default": "{}"
    },
    {
        "field": "config",
        "type": "dict",
        "optional": True,
        "default": "{}"
    },
    {
        "field": "tags.values",
        "type": "Tuple[str, ...]",
        "optional": True,
        "default": "()"
    },
    {
        "field": "tags.count",
        "type": "int",
        "optional": True,
        "default": "0"
    },
    {
        "field": "aux",
        "type": "dict",
        "optional": True,
        "default": "{}"
    },
    {
        "field": "data",
        "type": "dict",
        "optional": True,
        "default": "{}"
    },
    {
        "field": "device.name",
        "type": "str",
        "optional": True,
        "default": "NULL"
    },
    {
        "field": "device.brand",
        "type": "str",
        "optional": True,
        "default": "NULL"
    },
    {
        "field": "device.model",
        "type": "str",
        "optional": True,
        "default": "NULL"
    },
    {
        "field": "device.type",
        "type": "str",
        "optional": True,
        "default": "NULL"
    },
    {
        "field": "device.touch",
        "type": "bool",
        "optional": True,
        "default": "False"
    },
    {
        "field": "device.ip",
        "type": "str",
        "optional": True,
        "default": "NULL"
    },
    {
        "field": "device.resolution",
        "type": "str",
        "optional": True,
        "default": "NULL"
    },
    {
        "field": "device.geo.country.name",
        "type": "str",
        "optional": True,
        "default": "NULL"
    },
    {
        "field": "device.geo.country.code",
        "type": "str",
        "optional": True,
        "default": "NULL"
    },
    {
        "field": "device.geo.city",
        "type": "str",
        "optional": True,
        "default": "NULL"
    },
    {
        "field": "device.geo.county",
        "type": "str",
        "optional": True,
        "default": "NULL"
    },
    {
        "field": "device.geo.postal",
        "type": "str",
        "optional": True,
        "default": "NULL"
    },
    {
        "field": "device.geo.latitude",
        "type": "float",
        "optional": True,
        "default": "NULL"
    },
    {
        "field": "device.geo.longitude",
        "type": "float",
        "optional": True,
        "default": "NULL"
    },
    {
        "field": "device.color_depth",
        "type": "int",
        "optional": True,
        "default": "NULL"
    },
    {
        "field": "device.orientation",
        "type": "str",
        "optional": True,
        "default": "NULL"
    },
    {
        "field": "os.name",
        "type": "str",
        "optional": True,
        "default": "NULL"
    },
    {
        "field": "os.version",
        "type": "str",
        "optional": True,
        "default": "NULL"
    },
    {
        "field": "app.type",
        "type": "str",
        "optional": True,
        "default": "NULL"
    },
    {
        "field": "app.name",
        "type": "str",
        "optional": True,
        "default": "NULL"
    },
    {
        "field": "app.version",
        "type": "str",
        "optional": True,
        "default": "NULL"
    },
    {
        "field": "app.language",
        "type": "str",
        "optional": True,
        "default": "NULL"
    },
    {
        "field": "app.bot",
        "type": "bool",
        "optional": True,
        "default": "False"
    },
    {
        "field": "app.resolution",
        "type": "str",
        "optional": True,
        "default": "NULL"
    },
    {
        "field": "hit.name",
        "type": "str",
        "optional": True,
        "default": "NULL"
    },
    {
        "field": "hit.url",
        "type": "str",
        "optional": True,
        "default": "NULL"
    },
    {
        "field": "hit.referer",
        "type": "str",
        "optional": True,
        "default": "NULL"
    },
    {
        "field": "hit.query",
        "type": "str",
        "optional": True,
        "default": "NULL"
    },
    {
        "field": "hit.category",
        "type": "str",
        "optional": True,
        "default": "NULL"
    },
    {
        "field": "journey.state",
        "type": "str",
        "optional": True,
        "default": "NULL"
    }
]


