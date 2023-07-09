from ninja import Router, Query
from ninja.pagination import paginate
import logging
from django.http import Http404
from typing import List

from reservation_system.schemas.owner import (
    OwnerSchema,
    CreateOwnerSchema,
    PatchOwnerSchema,
)
from reservation_system.cruds.owner import owner_crud
from reservation_system.cruds.reservation import reservation_crud
from reservation_system.exceptions.exceptions import OwnerObjectDoesNotExist

logger = logging.getLogger(__name__)

router = Router()


@router.post("/create", response={201: OwnerSchema}, url_name="create-owner")
def create_owner(request, owner: CreateOwnerSchema):
    owner = owner_crud.create(owner)
    return owner


@router.get("/{int:owner_id}", response=OwnerSchema, url_name="retrieve-owner")
def retrieve_owner(request, owner_id):
    owner = owner_crud.get(owner_id)
    if not owner:
        raise OwnerObjectDoesNotExist
    return owner


@router.put("/{int:owner_id}", response=CreateOwnerSchema, url_name="put-owner")
def put_owner(request, owner_id, obj_in: CreateOwnerSchema):
    owner = owner_crud.get(owner_id)
    if not owner:
        raise OwnerObjectDoesNotExist
    owner = owner_crud.update(owner, obj_in)
    return owner


@router.patch("/{int:owner_id}", response=CreateOwnerSchema, url_name="patch-owner")
def patch_owner(request, owner_id, obj_in: PatchOwnerSchema):
    owner = owner_crud.get(owner_id)
    if not owner:
        raise OwnerObjectDoesNotExist
    owner = owner_crud.update(owner, obj_in)
    return owner


@router.delete("/{int:owner_id}", response={204: None}, url_name="patch-owner")
def delete_owner(request, owner_id):
    owner = owner_crud.get(owner_id)
    if not owner:
        raise OwnerObjectDoesNotExist
    owner_crud.delete(owner_id)

    return 204, None
