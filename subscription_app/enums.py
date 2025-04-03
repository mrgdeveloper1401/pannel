from django.db import models


class VolumeChoices(models.TextChoices):
    MG = 'mg'
    GB = "gb"
    TRA = 'tra'