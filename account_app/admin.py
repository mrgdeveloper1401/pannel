from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.core.exceptions import PermissionDenied
from django.utils.translation import gettext_lazy as _


from . import models
from . import forms
# Register your models here.


class NumberOfDaysFilter(admin.SimpleListFilter):
    title = _("Number of days")
    parameter_name = 'number_of_days'

    def lookups(self, request, model_admin):
        return [
            ("false", _("number of days is false"))
        ]

    def queryset(self, request, queryset):
        if self.value() == 'false':
            return queryset.filter(number_of_days__isnull=False)


class ContentDeviceInline(admin.TabularInline):
    model = models.ContentDevice
    extra = 1


@admin.register(models.User)
class UserAdmin(BaseUserAdmin):
    add_form = forms.UserAccountCreationForm
    change_password_form = forms.UserAdminPasswordChangeForm
    list_display = ("username", "is_staff", "is_active", "is_connected_user", "start_premium", "volume",
                    "volume_usage", "account_type", "accounts_status", "number_of_days",
                    "day_left", "number_of_max_device", "end_date_subscription", "remaining_volume_amount")
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "usable_password", "password1", "password2", "volume", "volume_choice",
                           "number_of_days", "start_premium", "number_of_max_device", "account_type", "accounts_status",
                           "user_type", "is_inf_volume", "is_staff", "groups", "user_permissions")
            },
        ),
    )
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email", "mobile_phone", "account_type",
                                         "accounts_status", "volume", "volume_usage", "all_volume_usage",
                                         "number_of_login", "number_of_days", "volume_choice", "is_inf_volume",
                                         "number_of_max_device", "fcm_token", "user_type", "created_by")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "is_connected_user",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined", "start_premium")}),
    )
    inlines = [ContentDeviceInline]
    list_filter = ('is_active', "is_staff", "is_superuser", "account_type", "accounts_status", NumberOfDaysFilter,
                   "user_type")
    readonly_fields = ["date_joined", "last_login", "account_type", "accounts_status",
                       "all_volume_usage", 'number_of_login']
    list_per_page = 20
    search_fields = ['username']
    ordering = ['-date_joined']
    raw_id_fields = ['created_by']

    def save_model(self, request, obj, form, change):
        if change:
            if not request.user.is_superuser:
                request_user_type = request.user.user_type
                get_user_type = form.cleaned_data.get("user_type")
                if get_user_type != request_user_type:
                    if not request.user.is_superuser:
                        raise PermissionDenied("you not permission this field user_type")
        if obj.id is None:
            if not request.user.is_superuser:
                obj.user_type = request.user.user_type
        if not change:
            obj.created_by = request.user
        return super().save_model(request, obj, form, change)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if not request.user.is_superuser:
            qs = qs.filter(user_type=request.user.user_type, created_by=request.user)
        return qs

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        is_superuser = request.user.is_superuser

        if not is_superuser:
            if request.user.has_perm("accounts.change_user"):
                fields_to_disable = [
                    'is_superuser',
                    'is_staff',
                    'is_connected_user',
                    'start_premium',
                    'is_inf_volume',
                    'fcm_token',
                    'user_type',
                    'groups',
                    'user_permissions',
                    "created_by"
                ]

                for field_name in fields_to_disable:
                    if field_name in form.base_fields:
                        form.base_fields[field_name].disabled = True
        return form

    def has_delete_permission(self, request, obj=None):
        if not request.user.is_superuser:
            if obj:
                if obj.is_staff and request.user.is_staff:
                    return False
        return super().has_delete_permission(request, obj)


@admin.register(models.ContentDevice)
class ContentDeviceAdmin(admin.ModelAdmin):
    pass
