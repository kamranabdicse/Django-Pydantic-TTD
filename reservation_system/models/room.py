from django.db import models
from .base import PersistanceModel
from .listing import Listing


class Room(PersistanceModel):
    number = models.IntegerField(null=False)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.FloatField(default=0.0)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name
