# from datetime import date, timedelta

# from django.utils import timezone
from django.core.exceptions import PermissionDenied
from django.core.validators import MinValueValidator
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from core_app.models import CommonColumnMixin
from account_app.enums import AccountType, AccountStatus, UserTypeChoices


# Create your models here.
class User(AbstractUser, CommonColumnMixin):
    mobile_phone = models.CharField(max_length=15, blank=True, null=True, unique=True,
                                    help_text=_("شماره موبایل کاربر"))
    account_type = models.CharField(max_length=15, choices=AccountType.choices, default=AccountType.normal_user,
                                    help_text=_("نوع اکانت"))
    accounts_status = models.CharField(max_length=15, choices=AccountStatus.choices, default=AccountStatus.NOTHING,
                                       help_text=_("active --> حجم و تاریخ انتقضای کانفینگ کاربر فعال هسنن \n"
                                                   "limit --> لیمیت یعنی کاربر حجمش تموم شده هست \n"
                                                   "expire --> یعنی کاربر روز کانفینگ ان تموم شده هست"))
    # volume_choice = models.CharField(max_length=7, choices=VolumeChoices.choices, default=VolumeChoices.GB)
    # volume = models.PositiveIntegerField(validators=[MinValueValidator(0)], help_text=_("کاربر چقدر حجم داشته باشد"),
    #                                      default=0)
    # volume_usage = models.FloatField(blank=True, default=0, help_text=_("حجم مصرفی میباشد که بر اساس مگابایت هست"),
    #                                  validators=[MinValueValidator(0)])
    # is_inf_volume = models.BooleanField(default=False, help_text=_("ایا حجم کاربر نامحدود باشد!"))
    all_volume_usage = models.FloatField(default=0, validators=[MinValueValidator(0)], editable=False,
                                         help_text=_("کاربر تا الان چقدر حجم مصرف کرده بر اساس مگابایت"))
    # start_premium = models.DateField(blank=True, null=True, help_text=_("تاریخ شروع اشتراک اگر کاربر لاگین کند"
    #                                                                     " اشتراک کاربر از همان روز شروع خواهد شد"))
    # number_of_days = models.PositiveIntegerField(help_text=_("تعداد روز"), null=True, default=0)
    number_of_login = models.PositiveIntegerField(help_text=_("تعداد لاگین های کاربر"), editable=False, default=0)
    is_connected_user = models.BooleanField(default=False, editable=False,
                                            help_text=_("این فیلد مشخص میکنه"
                                                        " که کاربر ایا به کانفیگش متصل شده هست یا خیر"))
    number_of_max_device = models.PositiveIntegerField(default=1,
                                                       help_text=_("هر اکانت چند تا یوزر میتواند به ان متصل شود"))
    fcm_token = models.CharField(max_length=255, blank=True, null=True, help_text=_("fcm token"))
    user_type = models.CharField(choices=UserTypeChoices, max_length=14, default=UserTypeChoices.tunnel_direct,
                                 help_text=_("you can choice --> tunnel - direct - tunnel_direct"))
    created_by = models.ForeignKey('self', related_name="owner", on_delete=models.DO_NOTHING, blank=True,
                                   null=True)
    REQUIRED_FIELDS = ('mobile_phone', "user_type")
    date_joined = None

    # @property
    # def end_date_subscription(self):
    #     if self.start_premium is not None and self.number_of_days is not None:
    #         return self.start_premium + timezone.timedelta(days=self.number_of_days)
    #     return None

    # @property
    # def remaining_volume_amount(self):
    #     if self.volume_choice == VolumeChoices.GB:
    #         remaining = self.volume - (self.volume_usage / 1000)
    #     elif self.volume_choice == VolumeChoices.MG:
    #         remaining = self.volume - self.volume_usage
    #     else:
    #         remaining = self.volume - (self.volume_usage / 1_000_000)
    #     if self.is_inf_volume:
    #         return "inf"
    #     return f'{remaining}, {self.volume_choice}'

    # @property
    # def day_left(self):
    #     if self.account_type == AccountType.premium_user:
    #         reminder_day = (self.end_date_subscription - date.today()).days
    #         return max(reminder_day, 0)
    #     return None

    # def clean(self):
    #     if self.volume > 0 and self.is_inf_volume:
    #         raise ValidationError({"volume": _("volume and is_inf volume they can't be together")})

    # def save(self, *args, **kwargs):
    #     # اگر کاربر لاگین کند برای بار اول تاریخ شروع اکانت مشخص خواهد شد
    #     if self.number_of_login == 1 and not self.start_premium:
    #         self.start_premium = date.today()
    #
    #     if self.start_premium:
    #         if self.volume_choice == VolumeChoices.GB:
    #             if self.volume_usage / 1_000 == self.volume:
    #                 self.account_type = AccountType.normal_user
    #                 self.accounts_status = AccountStatus.LIMIT
    #             if self.volume_usage / 1_000 < self.volume and self.number_of_login > 0:
    #                 self.account_type = AccountType.premium_user
    #                 self.accounts_status = AccountStatus.ACTIVE
    #             if self.start_premium + timedelta(days=self.number_of_days) < date.today():
    #                 self.account_type = AccountType.normal_user
    #                 self.accounts_status = AccountStatus.EXPIRED
    #
    #         if self.volume_choice == VolumeChoices.MG:
    #             if self.volume_usage == self.volume:
    #                 self.account_type = AccountType.normal_user
    #                 self.accounts_status = AccountStatus.LIMIT
    #             if self.volume_usage < self.volume and self.number_of_login > 0:
    #                 self.account_type = AccountType.premium_user
    #                 self.accounts_status = AccountStatus.ACTIVE
    #             if self.start_premium + timedelta(days=self.number_of_days) < date.today():
    #                 self.account_type = AccountType.normal_user
    #                 self.accounts_status = AccountStatus.EXPIRED
    #
    #         if self.volume_choice == VolumeChoices.TRA:
    #             if self.volume_usage / 1_000_000 == self.volume:
    #                 self.account_type = AccountType.normal_user
    #                 self.accounts_status = AccountStatus.LIMIT
    #             if self.volume_usage / 1_000_000 < self.volume and self.number_of_login > 0:
    #                 self.account_type = AccountType.premium_user
    #                 self.accounts_status = AccountStatus.ACTIVE
    #             if self.start_premium + timedelta(days=self.number_of_days) < date.today():
    #                 self.account_type = AccountType.normal_user
    #                 self.accounts_status = AccountStatus.EXPIRED
    #         if self.is_inf_volume:
    #             self.accounts_status = AccountStatus.ACTIVE
    #             self.account_type = AccountType.premium_user
    #
    #     else:
    #         self.account_type = AccountType.normal_user
    #         self.accounts_status = AccountStatus.NOTHING
    #     super().save(*args, **kwargs)

    class Meta:
        db_table = 'auth_user'


class ContentDevice(CommonColumnMixin):
    device_model = models.CharField(max_length=255, help_text=_("مدل دستگاه"), blank=True, null=True)
    device_os = models.CharField(max_length=50, help_text=_("نسخه دستگاه"), blank=True, null=True)
    device_number = models.CharField(max_length=255, help_text=_("سریال گوشی"), unique=True)
    ip_address = models.GenericIPAddressField(help_text=_("ادرس ای پی"))
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='user_device',
                             help_text=_("کاربر"))
    is_blocked = models.BooleanField(default=False, help_text=_("بلاک شدن"))

    def __str__(self):
        return f'{self.device_model} {self.device_os} {self.ip_address}'

    # def save(self, *args, **kwargs):
    #     if self.user.user_device.count() >= self.user.number_of_max_device:
    #         if not self.pk:
    #             raise PermissionDenied('your account max device connection has arrived')
    #     return super().save(*args, **kwargs)

    class Meta:
        db_table = 'content_device'
