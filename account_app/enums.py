from django.db import models
from django.utils.translation import gettext_lazy as _


class AccountType(models.TextChoices):
    normal_user = "normal_user"
    premium_user = "premium_user"


class AccountStatus(models.TextChoices):
    ACTIVE = "active"
    LIMIT = "limit"
    EXPIRED = "expired"
    NOTHING = "nothing"


class VolumeChoices(models.TextChoices):
    MG = 'mg'
    GB = "gb"
    TRA = 'tra'


class UserTypeChoices(models.TextChoices):
    direct = "direct", _("ستقیم")
    tunnel = "tunnel", _("تانل")
    tunnel_direct = "tunnel_direct", _("تانل دایرکت")
