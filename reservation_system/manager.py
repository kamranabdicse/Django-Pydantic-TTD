from django.db import models


class PersistanceModelManager(models.Manager):
    """Customizing <>.object.<> query-set for logical delete activated models"""

    def get_queryset(self):
        # equivalent:
        # Model.objects.filter(my-field=something, is_deleted=False)
        return super().get_queryset().filter(deleted_at__isnull=True)
