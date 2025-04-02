from django.db import models
from django.utils.translation import gettext_lazy as _


class TypeServerEnum(models.TextChoices):
    dedicated = 'dedicated', _("اختصاصی")
    shared = 'shared', _("اشتراکی")
    fast = "fast", _("پر سرعت")
