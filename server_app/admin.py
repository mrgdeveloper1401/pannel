from django.contrib import admin

from . import models
# Register your models here.


@admin.register(models.Country)
class CountryAdmin(admin.ModelAdmin):
    raw_id_fields = ("country_logo",)
    list_filter = ("is_publish",)
    list_per_page = 20

    def get_queryset(self, request):
        return super().get_queryset(request).only(
            "en_country_name", "fa_country_name", "country_logo", "is_publish"
        )


@admin.register(models.Server)
class ServerAdmin(admin.ModelAdmin):
    raw_id_fields = ("country",)
    list_per_page = 20
    list_filter = ("is_publish",)

    def get_queryset(self, request):
        return super().get_queryset(request).only(
            "country", "service_name", "is_publish", "server_type"
        )
