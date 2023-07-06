from django.db import models
from reservation_system.models.base import PersistanceModel


class Listing(PersistanceModel):
    # owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    owner = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name
