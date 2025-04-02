from django.contrib import admin

from . import models
# Register your models here.


@admin.register(models.Reseller)
class ResellerAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        return super().get_queryset(request).only(
            "user__first_name", "company_name", "phone", "email", "is_active", "max_users", "can_create_servers",
            "allowed_countries", "custom_logo", "primary_color", "custom_welcome_message", "commission_rate",
            "balance", "user__last_name"
        )

    raw_id_fields = ('custom_logo', "user")
    list_select_related = ("user", )
