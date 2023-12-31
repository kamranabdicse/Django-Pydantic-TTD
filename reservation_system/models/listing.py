from django.db import models
from .base import PersistanceModel


class Listing(PersistanceModel):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name
