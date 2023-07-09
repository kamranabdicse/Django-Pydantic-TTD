from ninja import Router, Query
from ninja.pagination import paginate
import logging
from django.http import Http404
from datetime import datetime
from reservation_system.exceptions.exceptions import ReservationObjectExist
from typing import List

from reservation_system.schemas.reservation import (
    MakeReservationSchemaIn,
    MakeReservationSchemaOut,
)
from reservation_system.cruds.reservation import reservation_crud
from reservation_system.cruds.room import room_crud
from reservation_system.schemas.reservation import BookRoomSchema

logger = logging.getLogger(__name__)

router = Router()


@router.post(
    "/make-reservation", response={201: MakeReservationSchemaOut}, url_name="make-reservation"
)
def make_reservation(request, reservation: MakeReservationSchemaIn):
    if reservation_crud.duplicate_reservation(
        reservation.room_id, reservation.check_in, reservation.check_out
    ):
        raise ReservationObjectExist
    
    room = room_crud.get(reservation.room_id)
    
    updated_reservation = MakeReservationSchemaIn(
        **reservation.dict(), price=room.price
    )
    reservation = reservation_crud.create(updated_reservation)
    return {"reservation_id": reservation.id, "price": reservation.price}



@router.get("/{int:listing_id}/{int:owner_id}", response=List[BookRoomSchema], url_name="booked-room-by-listing")
def booked_room_by_listing_id(request, listing_id, owner_id):
    reservations = reservation_crud.booked_for(listing_id, owner_id=owner_id)
    output = [
        {
            "reservation_id": reservation.id,
            "room_id": reservation.room.id,
            "room_number": reservation.room.number,
            "room_name": reservation.room.name,
            "check_in": reservation.check_in,
            "check_out": reservation.check_out,
            "reservation_time": reservation.reservation_time,
            "reservation_price": reservation.price,
            "listing_name": reservation.room.listing and reservation.room.listing.name,
            "listing_address": reservation.room.listing
            and reservation.room.listing.address,
            "listing_description": reservation.room.listing
            and reservation.room.listing.description,
            "owner_name": reservation.room.owner and reservation.room.owner.name,
            "owner_address": reservation.room.owner and reservation.room.owner.address,
        }
        for reservation in reservations
    ]
    return output