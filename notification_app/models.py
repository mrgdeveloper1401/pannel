from django.db import models

from core_app.models import CommonColumnMixin


# Create your models here.

class ResellerNotification(CommonColumnMixin):
    reseller = models.ForeignKey(
        "representative_app.Reseller",
        on_delete=models.DO_NOTHING,
        related_name="reseller_notifications"
    )
    message = models.TextField()
    is_read = models.BooleanField(default=False)

    class Meta:
        db_table = 'reseller_notifications'
