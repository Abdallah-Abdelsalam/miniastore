# Generated by Django 5.0.1 on 2024-03-19 18:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("product", "0005_brand_delete_brands_product_brand"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="color",
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name="product",
            name="size",
            field=models.CharField(blank=True, max_length=10),
        ),
    ]