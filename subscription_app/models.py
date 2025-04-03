from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from core_app.models import CommonColumnMixin
from subscription_app.enums import VolumeChoices


# Create your models here.


class Subscription(CommonColumnMixin):
    user = models.ForeignKey('account_app.User', on_delete=models.PROTECT, related_name='subscriptions')
    volume_choice = models.CharField(max_length=7, choices=VolumeChoices.choices, default=VolumeChoices.GB)
    volume = models.PositiveIntegerField(validators=[MinValueValidator(0)], help_text=_("کاربر چقدر حجم داشته باشد"),
                                         default=0)
    is_inf_volume = models.BooleanField(default=False, help_text=_("ایا حجم کاربر نامحدود باشد!"))
    start_premium = models.DateField(blank=True, null=True, help_text=_("تاریخ شروع اشتراک اگر کاربر لاگین کند"
                                                                        " اشتراک کاربر از همان روز شروع خواهد شد"))
    number_of_days = models.PositiveIntegerField(help_text=_("تعداد روز"), null=True, default=0)
