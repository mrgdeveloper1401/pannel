from django.contrib import admin

from . import models
# Register your models here.


@admin.register(models.Images)
class ImagesAdmin(admin.ModelAdmin):
    list_per_page = 20

    def get_queryset(self, request):
        return super().get_queryset(request).only(
            "image", "image_size", "image_width", "image_height", "image_name"
        )
