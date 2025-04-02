from django.db import models
from django.utils.translation import gettext_lazy as _

from core_app.models import CommonColumnMixin
from server_app.enums import TypeServerEnum


class Country(CommonColumnMixin):
    en_country_name = models.CharField(max_length=50)
    fa_country_name = models.CharField(max_length=50)
    country_logo = models.ForeignKey("image_app.Images", on_delete=models.SET_NULL, null=True, blank=True)
    is_publish = models.BooleanField(default=True)

    class Meta:
        db_table = 'country'
        verbose_name_plural = _("Countries")


class Server(CommonColumnMixin):
    country = models.ForeignKey(Country, on_delete=models.PROTECT, limit_choices_to={"is_publish": True})
    service_name = models.CharField(max_length=255)
    is_publish = models.BooleanField(default=True)
    server_type = models.CharField(choices=TypeServerEnum.choices, max_length=10)

    class Meta:
        db_table = 'service'
