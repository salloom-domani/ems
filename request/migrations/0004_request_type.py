# Generated by Django 4.1a1 on 2022-07-22 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("request", "0003_remove_request_type"),
    ]

    operations = [
        migrations.AddField(
            model_name="request",
            name="type",
            field=models.CharField(default="transferrequest", max_length=50),
            preserve_default=False,
        ),
    ]
