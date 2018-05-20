# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-02 20:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_city', models.CharField(max_length=45)),
                ('code_area', models.CharField(blank=True, max_length=45, null=True)),
                ('code_postal', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'city',
                'managed': False,
            },
        ),
    ]
