# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-10 08:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0002_restaurent_location'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Restaurent',
            new_name='RestaurantLocation',
        ),
    ]
