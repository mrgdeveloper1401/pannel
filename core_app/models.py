from django.db import models
from django.utils import timezone

from core_app.managers import CommonColumnManager


class CommonColumnMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    is_deleted = models.BooleanField(editable=False, null=True)
    deleted_at = models.DateTimeField(editable=False, null=True)

    objects = CommonColumnManager()

    class Meta:
        abstract = True

    def delete(self, using=None, keep_parents=False):
        self.deleted_at = timezone.now()
        self.is_deleted = True
        self.save()
