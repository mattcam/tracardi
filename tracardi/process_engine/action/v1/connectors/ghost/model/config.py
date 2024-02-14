from pydantic import field_validator

from tracardi.domain.named_entity import NamedEntity
from tracardi.service.plugin.domain.config import PluginConfig


class Configuration(PluginConfig):
    source: NamedEntity
    label_add: str
    label_remove: str
    uuid: str

    @field_validator('uuid')
    @classmethod
    def must_not_be_emty(cls, value):
        if value.strip() == "":
            raise ValueError("UUID must not be empty.")
        return value