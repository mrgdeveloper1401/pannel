# Generated by Django 5.1.7 on 2025-04-02 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Images",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("is_deleted", models.BooleanField(editable=False, null=True)),
                ("deleted_at", models.DateTimeField(editable=False, null=True)),
                (
                    "image",
                    models.ImageField(
                        height_field="image_width",
                        upload_to="images/%Y/%m/%d/",
                        width_field="image_height",
                    ),
                ),
                ("image_size", models.PositiveIntegerField(blank=True, null=True)),
                ("image_width", models.PositiveIntegerField(blank=True, null=True)),
                ("image_height", models.PositiveIntegerField(blank=True, null=True)),
                ("image_name", models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                "verbose_name": "Image",
                "verbose_name_plural": "Images",
                "db_table": "images",
            },
        ),
    ]
