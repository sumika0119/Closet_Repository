# Generated by Django 4.2.7 on 2023-12-25 11:06

import datetime
import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0002_useractivatetokens"),
    ]

    operations = [
        migrations.AlterModelManagers(
            name="users",
            managers=[
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name="users",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True,
                default=datetime.datetime(
                    2023, 12, 25, 11, 6, 25, 801295, tzinfo=datetime.timezone.utc
                ),
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="users",
            name="updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
