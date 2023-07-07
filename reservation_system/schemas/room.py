from typing import Optional
from ninja import ModelSchema, Schema
from reservation_system.models import Room


class RoomSchema(Schema):
    id: int
    listing_id: int
    owner_id: int
    number: int
    name: Optional[str]
    price: float


class CreateRoomSchema(Schema):
    listing_id: int
    owner_id: int
    number: int
    name: Optional[str]
    price: float


class PutRoomSchema(Schema):
    number: int
    name: str
    price: float


class PatchRoomSchema(Schema):
    number: Optional[int]
    name: Optional[str]
    price: Optional[float]
