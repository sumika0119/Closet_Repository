# Generated by Django 4.2.7 on 2024-01-02 14:18

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0004_alter_users_managers"),
    ]

    operations = [
        migrations.AlterField(
            model_name="users",
            name="is_superuser",
            field=models.BooleanField(default=False),
        ),
    ]