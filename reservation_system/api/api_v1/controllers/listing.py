from ninja import Router, Query
from ninja.pagination import paginate
import logging
from django.http import Http404
from typing import List

from reservation_system.schemas.listing import (
    ListingSchema,
    CreateListingSchema,
    PatchListingSchema,
)

from reservation_system.cruds.listing import listing_crud
from reservation_system.cruds.reservation import reservation_crud
from reservation_system.exceptions.exceptions import ListingObjectDoesNotExist

logger = logging.getLogger(__name__)

router = Router()


@router.post("/create", response={201: ListingSchema}, url_name="create-listing")
def create_listing(request, listing: CreateListingSchema):
    listing = listing_crud.create(listing)
    return listing


@router.get("/{int:listing_id}", response=ListingSchema, url_name="retrieve-listing")
def retrieve_listing(request, listing_id):
    listing = listing_crud.get(listing_id)
    if not listing:
        raise ListingObjectDoesNotExist
    return listing


@router.put("/{int:listing_id}", response=CreateListingSchema, url_name="put-listing")
def put_listing(request, listing_id, obj_in: CreateListingSchema):
    listing = listing_crud.get(listing_id)
    if not listing:
        raise ListingObjectDoesNotExist
    listing = listing_crud.update(listing, obj_in)
    return listing


@router.patch(
    "/{int:listing_id}", response=CreateListingSchema, url_name="patch-listing"
)
def patch_listing(request, listing_id, obj_in: PatchListingSchema):
    listing = listing_crud.get(listing_id)
    if not listing:
        raise ListingObjectDoesNotExist
    listing = listing_crud.update(listing, obj_in)
    return listing


@router.delete("/{int:listing_id}", response={204: None}, url_name="patch-listing")
def delete_listing(request, listing_id):
    listing = listing_crud.get(listing_id)
    if not listing:
        raise ListingObjectDoesNotExist
    listing_crud.delete(listing_id)

    return 204, None
