from django.db import models
from .base import PersistanceModel
from .listing import Listing
from .owner import Owner


class Room(PersistanceModel):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    number = models.IntegerField(null=False)
    name = models.CharField(max_length=100)
    price = models.FloatField(default=0.0)

    def __str__(self):
        return self.name
