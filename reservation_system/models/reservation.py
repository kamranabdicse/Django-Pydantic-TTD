from django.db import models
from .base import PersistanceModel
from .room import Room


class Reservation(PersistanceModel):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()
    reservation_time = models.DateTimeField(null=True)
    price = models.FloatField(default=0.0)

    def __str__(self):
        return self.name
