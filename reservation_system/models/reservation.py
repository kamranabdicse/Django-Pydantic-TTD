from django.db import models
from .base import PersistanceModel
from .room import Room


class Reservation(PersistanceModel):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    status_choices = models.TextChoices(
        "status",
        "choose payment_pending purchased",
    )
    status = models.CharField(
        max_length=20,
        choices=status_choices.choices,
        default=status_choices.choose.value,
    )
    choose_time = models.DateTimeField(null=True)
    purchased_time = models.DateTimeField(null=True)
    tax_price = models.FloatField(default=0.0)
    discount_price = models.FloatField(default=0.0)
    price = models.FloatField(default=0.0)

    def __str__(self):
        return self.name
