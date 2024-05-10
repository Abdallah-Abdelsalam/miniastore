# Generated by Django 5.0.1 on 2024-03-16 00:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("product", "0003_rename_category_product_category_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Brands",
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
                ("name", models.CharField(max_length=255)),
                ("slug", models.SlugField()),
            ],
            options={
                "ordering": ("name",),
            },
        ),
    ]
