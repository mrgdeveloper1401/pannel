from django.db import models
from django.utils.translation import gettext_lazy as _

from core_app.models import CommonColumnMixin


class Images(CommonColumnMixin):
    image = models.ImageField(upload_to='images/%Y/%m/%d/', height_field="image_width", width_field="image_height")
    image_size = models.PositiveIntegerField(blank=True, null=True)
    image_width = models.PositiveIntegerField(blank=True, null=True)
    image_height = models.PositiveIntegerField(blank=True, null=True)
    image_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'images'
        verbose_name = _("Image")
        verbose_name_plural = _("Images")

    def save(self, *args, **kwargs):
        self.image_size = self.image.size
        self.image_name = self.image.name
        super().save(*args, **kwargs)
