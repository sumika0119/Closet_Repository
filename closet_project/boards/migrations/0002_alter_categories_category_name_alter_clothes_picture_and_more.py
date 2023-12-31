# Generated by Django 4.2.7 on 2023-12-28 11:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("boards", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="categories",
            name="category_name",
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name="clothes",
            name="picture",
            field=models.ImageField(blank=True, null=True, upload_to=""),
        ),
        migrations.AlterField(
            model_name="clothes",
            name="price",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=10, null=True
            ),
        ),
        migrations.AlterField(
            model_name="clothes",
            name="purchase_data",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="clothes",
            name="store",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="boards.stores",
            ),
        ),
        migrations.AlterField(
            model_name="colors",
            name="color_name",
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name="stores",
            name="store_name",
            field=models.CharField(max_length=100),
        ),
        migrations.CreateModel(
            name="Clothe_Colors",
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
                (
                    "clothes",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="boards.clothes"
                    ),
                ),
                (
                    "colors",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="boards.colors"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="clothes",
            name="color",
            field=models.ManyToManyField(
                through="boards.Clothe_Colors", to="boards.colors"
            ),
        ),
    ]
