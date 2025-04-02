from django.db import models
from django.db.models import Q
from django.utils import timezone


class CommonColumnManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(Q(is_deleted=False) | Q(is_deleted=None), deleted_at=None)

    def delete(self):
        super().delete(is_deleted=True, deleted_at=timezone.now())
