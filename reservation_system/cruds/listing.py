from reservation_system.cruds.base import BaseCRUD
from reservation_system.models import Listing


class CrudListing(BaseCRUD):
    def create(self, obj_in):
        # Additional validation or customization before creating the listing
        return super().create(obj_in)

    def update(self, listing, obj_in=None):
        # Additional validation or customization before updating the listing
        return super().update(listing, obj_in)

    def delete(self, pk: int):
        # Additional validation or customization before deleting the listing
        return super().delete(pk)
    
    def get(self, pk: int):
        return super().get(pk)


listing_crud = CrudListing(Listing)