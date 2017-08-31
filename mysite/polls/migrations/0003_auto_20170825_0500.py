# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-25 05:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_document'),
    ]

    operations = [
        migrations.CreateModel(
            name='Privileges',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Privilege', models.CharField(max_length=40)),
            ],
        ),
        migrations.AlterField(
            model_name='document',
            name='document',
            field=models.FileField(upload_to='documents/%Y/%m/%d/'),
        ),
    ]