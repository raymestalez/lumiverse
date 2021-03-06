# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-12 22:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hub',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('slug', models.SlugField(default='', max_length=64)),
                ('avatar', models.ImageField(blank=True, default=None, null=True, upload_to='hubs/avatars/')),
                ('background', models.ImageField(blank=True, default=None, null=True, upload_to='hubs/backgrounds/')),
                ('description', models.TextField(blank=True, default='', null=True)),
            ],
        ),
    ]
