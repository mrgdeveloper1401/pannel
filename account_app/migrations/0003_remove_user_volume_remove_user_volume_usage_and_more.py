# Generated by Django 5.1.7 on 2025-04-03 10:45

import django.core.validators
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "account_app",
            "0002_remove_user_is_inf_volume_remove_user_number_of_days_and_more",
        ),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="volume",
        ),
        migrations.RemoveField(
            model_name="user",
            name="volume_usage",
        ),
        migrations.AddField(
            model_name="user",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="user",
            name="deleted_at",
            field=models.DateTimeField(editable=False, null=True),
        ),
        migrations.AddField(
            model_name="user",
            name="is_deleted",
            field=models.BooleanField(editable=False, null=True),
        ),
        migrations.AddField(
            model_name="user",
            name="updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name="user",
            name="account_type",
            field=models.CharField(
                choices=[
                    ("normal_user", "کاربر عادی"),
                    ("premium_user", "کاربر پریمیوم"),
                ],
                default="normal_user",
                help_text="نوع اکانت",
                max_length=15,
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="accounts_status",
            field=models.CharField(
                choices=[
                    ("active", "فعال"),
                    ("limit", "محدود شده"),
                    ("expired", "منقضی شده"),
                    ("nothing", "کاربر جدید"),
                ],
                default="nothing",
                help_text="active --> حجم و تاریخ انتقضای کانفینگ کاربر فعال هسنن \nlimit --> لیمیت یعنی کاربر حجمش تموم شده هست \nexpire --> یعنی کاربر روز کانفینگ ان تموم شده هست",
                max_length=15,
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="all_volume_usage",
            field=models.FloatField(
                default=0,
                editable=False,
                help_text="کاربر تا الان چقدر حجم مصرف کرده بر اساس مگابایت",
                validators=[django.core.validators.MinValueValidator(0)],
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="is_connected_user",
            field=models.BooleanField(
                default=False,
                editable=False,
                help_text="این فیلد مشخص میکنه که کاربر ایا به کانفیگش متصل شده هست یا خیر",
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="number_of_login",
            field=models.PositiveIntegerField(
                default=0, editable=False, help_text="تعداد لاگین های کاربر"
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="user_type",
            field=models.CharField(
                choices=[
                    ("direct", "مستقیم"),
                    ("tunnel", "تانل"),
                    ("tunnel_direct", "تانل دایرکت"),
                ],
                default="tunnel_direct",
                help_text="you can choice --> tunnel - direct - tunnel_direct",
                max_length=14,
            ),
        ),
    ]
