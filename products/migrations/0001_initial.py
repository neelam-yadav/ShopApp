# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import products.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=120)),
                ('image', models.ImageField(upload_to=products.models.image_upload_to)),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.DecimalField(max_digits=20, decimal_places=2)),
            ],
            options={
                'ordering': ['-title'],
            },
        ),
    ]
