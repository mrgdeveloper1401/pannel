from django.db import models
from django.utils.translation import gettext_lazy as _


class AccountType(models.TextChoices):
    normal_user = "normal_user", _("کاربر عادی")
    premium_user = "premium_user", _("کاربر پریمیوم")


class AccountStatus(models.TextChoices):
    ACTIVE = "active", _("فعال")
    LIMIT = "limit", _("محدود شده")
    EXPIRED = "expired", _("منقضی شده")
    NOTHING = "nothing", _("کاربر جدید")


# class VolumeChoices(models.TextChoices):
#     MG = 'mg'
#     GB = "gb"
#     TRA = 'tra'


class UserTypeChoices(models.TextChoices):
    direct = "direct", _("مستقیم")
    tunnel = "tunnel", _("تانل")
    tunnel_direct = "tunnel_direct", _("تانل دایرکت")
