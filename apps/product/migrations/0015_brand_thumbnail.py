# Generated by Django 5.0.1 on 2024-04-02 06:45

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("product", "0014_brand_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="brand",
            name="thumbnail",
            field=models.ImageField(blank=True, null=True, upload_to="uploads/"),
        ),
    ]
