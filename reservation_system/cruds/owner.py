from reservation_system.cruds.base import BaseCRUD
from reservation_system.models import Owner


class CrudOwner(BaseCRUD):
    def create(self, obj_in):
        # Additional validation or customization before creating the listing
        return super().create(obj_in)

    def update(self, owner, obj_in=None):
        # Additional validation or customization before updating the listing
        return super().update(owner, obj_in)

    def delete(self, pk: int):
        # Additional validation or customization before deleting the listing
        return super().delete(pk)

    def get(self, pk: int):
        return super().get(pk)


owner_crud = CrudOwner(Owner)
