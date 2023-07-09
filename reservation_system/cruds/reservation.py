from reservation_system.cruds.base import BaseCRUD
from reservation_system.models import Reservation
from datetime import datetime
from django.db.models import Q, Sum


class CrudReservation(BaseCRUD):
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

    def duplicate_reservation(
        self, room_id: int, check_in: datetime, check_out: datetime
    ) -> bool:
        query_params = (
            Q(check_out__gt=check_in) & Q(check_in__lt=check_out) & Q(room_id=room_id)
        )
        return self.model.objects.filter(query_params).exists()
    
    def booked_for(self, listing_id=None, owner_id=None):
        query_params = Q()
        if listing_id:
            query_params &= Q(room__listing_id=listing_id)
        if owner_id:
            query_params &= Q(room__owner_id=owner_id)
        return self.model.objects.filter(query_params)


reservation_crud = CrudReservation(Reservation)
