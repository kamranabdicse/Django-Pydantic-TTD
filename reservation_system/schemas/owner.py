from typing import Optional
from ninja import ModelSchema, Schema
from reservation_system.models import Owner


class OwnerSchema(ModelSchema):
    class Config:
        model = Owner
        model_exclude = ("created_at", "updated_at", "deleted_at")


class CreateOwnerSchema(ModelSchema):
    class Config:
        model = Owner
        model_exclude = ("id", "created_at", "updated_at", "deleted_at")


class PatchOwnerSchema(Schema):
    name: Optional[str]
    address: Optional[str]