from django.db import models
from .base import PersistanceModel


class Owner(PersistanceModel):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.name