# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-13 08:28
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('estore', '0008_auto_20170813_0824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='token',
            field=models.UUIDField(db_index=True, default=uuid.UUID('9f1c6d8d-eed0-4fd3-9a77-a6d9aa5f6936')),
        ),
    ]