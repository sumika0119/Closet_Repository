# Generated by Django 4.2.7 on 2024-01-21 01:57

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("boards", "0008_rename_purchase_data_clothes_purchase_date_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="clothes",
            name="picture",
            field=models.ImageField(
                blank=True, null=True, upload_to="closet_project/media/"
            ),
        ),
    ]
