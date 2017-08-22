# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-22 05:58
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('estore', '0009_auto_20170822_0533'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart_items',
            name='quantity',
        ),
        migrations.AlterField(
            model_name='order',
            name='token',
            field=models.UUIDField(db_index=True, default=uuid.UUID('12190a7d-ef2a-414d-bd05-f5005177da2f')),
        ),
    ]