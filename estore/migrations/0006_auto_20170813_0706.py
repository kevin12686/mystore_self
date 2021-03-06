# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-13 07:06
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('estore', '0005_order_token'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='is_paid',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='payment_method',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='order',
            name='token',
            field=models.UUIDField(db_index=True, default=uuid.UUID('5c3aa903-e1b3-4c58-ad66-be7d8ea9d8aa')),
        ),
    ]
