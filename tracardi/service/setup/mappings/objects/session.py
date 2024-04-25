session_properties = [
    {
        "field": "id",
        "type": "str",
        "optional": False,
        "default": None
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
        "field": "metadata.time.timestamp",
        "type": "float",
        "optional": True,
        "default": None
    },
    {
        "field": "metadata.time.duration",
        "type": "float",
        "optional": False,
        "default": 0
    },
    {
        "field": "metadata.time.weekday",
        "type": "int",
        "optional": True,
        "default": "self.insert.weekday()"
    },
    {
        "field": "metadata.channel",
        "type": "str",
        "optional": True,
        "default": "NULL"
    },
    {
        "field": "metadata.aux",
        "type": "dict",
        "optional": True,
        "default": {}
    },
    {
        "field": "metadata.status",
        "type": "str",
        "optional": True,
        "default": "NULL"
    },
    {
        "field": "operation.new",
        "type": "bool",
        "optional": False,
        "default": "False"
    },
    {
        "field": "operation.update",
        "type": "bool",
        "optional": False,
        "default": "False"
    },
    {
        "field": "profile.id",
        "type": "str",
        "optional": True,
        "default": None
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
        "field": "context",
        "type": "SessionContext",
        "optional": True,
        "default": {}
    },
    {
        "field": "properties",
        "type": "dict",
        "optional": True,
        "default": {}
    },
    {
        "field": "traits",
        "type": "dict",
        "optional": True,
        "default": {}
    },
    {
        "field": "aux",
        "type": "dict",
        "optional": True,
        "default": {}
    }
]
