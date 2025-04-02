from django.db import models
from django.utils.translation import gettext_lazy as _

from core_app.models import CommonColumnMixin


class Reseller(CommonColumnMixin):
    # اطلاعات پایه نماینده
    user = models.OneToOneField(
        "account_app.User",
        on_delete=models.PROTECT,
        verbose_name=_("حساب کاربری"),
        related_name="reseller"
    )
    company_name = models.CharField(
        max_length=100,
        verbose_name=_("نام شرکت/نماینده"),
    )
    phone = models.CharField(
        max_length=15,
        verbose_name=_("تلفن تماس"),
        unique=True
    )
    email = models.EmailField(
        verbose_name=_("ایمیل"),
        unique=True
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name=_("فعال/غیرفعال")
    )

    # تنظیمات دسترسی و محدودیت‌ها
    max_users = models.PositiveIntegerField(
        verbose_name=_("حداکثر کاربران مجاز")
    )
    can_create_servers = models.BooleanField(
        default=False,
        verbose_name=_("اجازه ایجاد سرور")
    )
    allowed_countries = models.JSONField(
        default=list,
        verbose_name=_("کشورهای مجاز برای فروش"),
        help_text=_("لیست کشورهایی که این نماینده می‌تواند سرور ارائه دهد.")
    )

    # شخصی‌سازی پنل نماینده
    custom_logo = models.ForeignKey(
        "image_app.Images",
        verbose_name=_("لوگوی اختصاصی"),
        on_delete=models.SET_NULL,
        null=True,
    )
    primary_color = models.CharField(
        max_length=7,
        default="#4a6bff",
        verbose_name=_("رنگ اصلی پنل")
    )
    custom_welcome_message = models.TextField(
        blank=True,
        verbose_name=_("پیام خوش‌آمدگویی اختصاصی")
    )

    # مالی و کمیسیون
    commission_rate = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=20.00,
        verbose_name=_("درصد کمیسیون (%)")
    )
    balance = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
        verbose_name=_("موجودی (ریال)")
    )

    class Meta:
        db_table = "reseller"

    def __str__(self):
        return f"{self.company_name or self.user.get_full_name()}"
