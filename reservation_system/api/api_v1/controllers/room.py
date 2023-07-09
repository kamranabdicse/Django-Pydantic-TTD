from ninja import Router, Query
from ninja.pagination import paginate
import logging
from django.http import Http404
from datetime import datetime
from typing import List

from reservation_system.schemas.room import (
    RoomSchema,
    CreateRoomSchema,
    PatchRoomSchema,
    PutRoomSchema,
)
from reservation_system.cruds.room import room_crud
from reservation_system.exceptions.exceptions import RoomObjectDoesNotExist

logger = logging.getLogger(__name__)

router = Router()


@router.post("/create", response={201: RoomSchema}, url_name="create-room")
def create_room(request, room: CreateRoomSchema):
    room = room_crud.create(room)
    return room


@router.get("/{int:room_id}", response=RoomSchema, url_name="retrieve-room")
def retrieve_room(request, room_id):
    room = room_crud.get(room_id)
    if not room:
        raise RoomObjectDoesNotExist
    return room


@router.put("/{int:room_id}", response=CreateRoomSchema, url_name="put-room")
def put_room(request, room_id, obj_in: PutRoomSchema):
    room = room_crud.get(room_id)
    if not room:
        raise RoomObjectDoesNotExist
    room = room_crud.update(room, obj_in)
    return room


@router.patch("/{int:room_id}", response=CreateRoomSchema, url_name="patch-room")
def patch_room(request, room_id, obj_in: PatchRoomSchema):
    room = room_crud.get(room_id)
    if not room:
        raise RoomObjectDoesNotExist
    room = room_crud.update(room, obj_in)
    return room


@router.delete("/{int:room_id}", response={204: None}, url_name="patch-room")
def delete_room(request, room_id):
    room = room_crud.get(room_id)
    if not room:
        raise RoomObjectDoesNotExist
    room_crud.delete(room_id)

    return 204, None


@router.get("/{check_in}/{check_out}/{count}", response=List[RoomSchema], url_name="check-available-room")
def check_available_room(request, check_in: str, check_out: str, count: int):
    try:
        print("------------")
        check_in = datetime.strptime(check_in, "%Y-%m-%d %H:%M")
        check_out = datetime.strptime(check_out, "%Y-%m-%d %H:%M")
        rooms = room_crud.available_rooms(check_in, check_out, count)
    except ValueError:
        raise Http404("Invalid datetime format")
    return rooms