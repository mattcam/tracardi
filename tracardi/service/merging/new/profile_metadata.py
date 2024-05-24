from typing import List, Any

from pydantic import BaseModel

from tracardi.service.merging.new.field_metadata import FieldMetaData


class ProfileMetaData(BaseModel):
    profile: Any  # Dotty
    fields_metadata: List[FieldMetaData]


    def merge(self):
        for field_metadata  in self.fields_metadata:
            print(self.profile['id'])
            print(self.fields())
            yield field_metadata.merge(self.profile)

    def fields(self):
        return [(field_meta.field, field_meta.field_values()) for field_meta in self.fields_metadata]