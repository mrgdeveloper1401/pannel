from django.contrib import admin

from . import models
# Register your models here.


@admin.register(models.Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    pass
