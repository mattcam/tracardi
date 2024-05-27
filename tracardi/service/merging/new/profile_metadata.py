from dotty_dict import Dotty
from typing import List, Any

from pydantic import BaseModel

from tracardi.service.merging.new.field_metadata import FieldMetaData


class ProfileMetaData(BaseModel):
    profiles: List # List[Dotty]
    fields_metadata: List[FieldMetaData]
    default_strategies: List[str]


    def merge(self):
        for field_metadata  in self.fields_metadata:
            yield field_metadata, field_metadata.merge(self.profiles, self.default_strategies)

    def fields(self):
        return [(field_meta.field, field_meta.field_values()) for field_meta in self.fields_metadata]

    def filter(self, field):
        return [item for item in self.fields_metadata if item.field==field]