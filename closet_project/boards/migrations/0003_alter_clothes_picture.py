# Generated by Django 4.2.7 on 2023-12-28 14:51

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "boards",
            "0002_alter_categories_category_name_alter_clothes_picture_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="clothes",
            name="picture",
            field=models.FileField(blank=True, null=True, upload_to=""),
        ),
    ]