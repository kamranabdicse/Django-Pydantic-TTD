from typing import Optional
from ninja import ModelSchema, Schema
from reservation_system.models import Listing


class ListingSchema(ModelSchema):
    class Config:
        model = Listing
        model_exclude = ("created_at", "updated_at", "deleted_at")


class CreateListingSchema(ModelSchema):
    class Config:
        model = Listing
        model_exclude = ("id", "created_at", "updated_at", "deleted_at")


class PatchListingSchema(Schema):
    owner: Optional[str]
    name: Optional[str]
    address: Optional[str]
    description: Optional[str]
