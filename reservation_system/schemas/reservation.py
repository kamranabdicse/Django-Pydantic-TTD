from typing import Optional
from ninja import ModelSchema, Schema
from reservation_system.models import Reservation
from datetime import datetime, date


class MakeReservationSchemaIn(Schema):
    room_id: int
    name: str
    check_in: datetime
    check_out: datetime
    reservation_time: datetime


class MakeReservationSchemaOut(Schema):
    reservation_id: int
    price: float


class BookRoomSchema(Schema):
    reservation_id: int
    room_id: int
    room_number: int
    room_name: str
    check_in: datetime
    check_out: datetime
    reservation_time: datetime
    reservation_price: float
    listing_name: str
    listing_address: str
    listing_description: str
    owner_name: str
    owner_address: str
