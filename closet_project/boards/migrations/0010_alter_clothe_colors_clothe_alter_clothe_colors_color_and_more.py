# Generated by Django 4.2.7 on 2024-01-23 11:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("boards", "0009_alter_clothes_picture"),
    ]

    operations = [
        migrations.AlterField(
            model_name="clothe_colors",
            name="clothe",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="clothe_color_relation",
                to="boards.clothes",
            ),
        ),
        migrations.AlterField(
            model_name="clothe_colors",
            name="color",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="color_clothe_relation",
                to="boards.colors",
            ),
        ),
        migrations.AlterField(
            model_name="clothes",
            name="color",
            field=models.ManyToManyField(
                null=True,
                related_name="clothe",
                through="boards.Clothe_Colors",
                to="boards.colors",
            ),
        ),
        migrations.AlterField(
            model_name="clothes",
            name="purchase_date",
            field=models.DateField(blank=True, null=True),
        ),
    ]