from django.contrib import admin

from . import models
# Register your models here.


@admin.register(models.ResellerNotification)
class ResellerNotificationAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        return super().get_queryset(request).only(
            "reseller", "message", "is_read"
        )

    raw_id_fields = ('reseller',)
