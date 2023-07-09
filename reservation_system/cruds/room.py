from reservation_system.cruds.base import BaseCRUD
from reservation_system.models import Room
from django.db.models import Q, Sum


class CrudRoom(BaseCRUD):
    def create(self, obj_in):
        # Additional validation or customization before creating the listing
        return super().create(obj_in)

    def update(self, room, obj_in=None):
        # Additional validation or customization before updating the listing
        return super().update(room, obj_in)

    def delete(self, pk: int):
        # Additional validation or customization before deleting the listing
        return super().delete(pk)

    def get(self, pk: int):
        return super().get(pk)

    def available_rooms(self, check_in, check_out, count):
        query_params = Q(reservation__check_out__gt=check_in) & Q(
            reservation__check_in__lt=check_out
        )
        return self.model.objects.exclude(query_params)[:count]


room_crud = CrudRoom(Room)
