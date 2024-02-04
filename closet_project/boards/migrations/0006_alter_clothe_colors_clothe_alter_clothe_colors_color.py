# Generated by Django 4.2.7 on 2023-12-30 08:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("boards", "0005_remove_clothe_colors_clothes_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="clothe_colors",
            name="clothe",
            field=models.ForeignKey(
                default=0,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="clothe_color",
                to="boards.clothes",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="clothe_colors",
            name="color",
            field=models.ForeignKey(
                default=0,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="clothe_colors",
                to="boards.colors",
            ),
            preserve_default=False,
        ),
    ]
