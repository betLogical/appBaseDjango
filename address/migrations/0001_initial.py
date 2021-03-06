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
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField()),
                ('race', models.CharField(blank=True, max_length=45, null=True)),
                ('street', models.CharField(blank=True, max_length=45, null=True)),
                ('avenue', models.CharField(blank=True, max_length=45, null=True)),
                ('sidewalk', models.CharField(blank=True, max_length=45, null=True)),
                ('building', models.CharField(blank=True, max_length=45, null=True)),
                ('floor', models.CharField(blank=True, max_length=45, null=True)),
                ('name_residence', models.CharField(blank=True, max_length=45, null=True)),
                ('number_residence', models.CharField(blank=True, max_length=45, null=True)),
                ('suburb', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'address',
                'managed': False,
            },
        ),
    ]
