from django.db import models
from django.utils import timezone

from reservation_system.manager import PersistanceModelManager


class BaseModel(models.Model):
    """Adding create and update fields to the model"""

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class PersistanceModel(BaseModel):
    """Adding logical delete functionality to the model"""

    deleted_at = models.DateTimeField(null=True, default=None)
    objects = PersistanceModelManager()
    all_objects = models.Manager()

    def delete(self):
        self.deleted_at = timezone.now()
        self.save()

    def restore(self):
        self.deleted_at = None
        self.save()

    class Meta:
        abstract = True









