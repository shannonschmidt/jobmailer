# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('signup_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('posting_date', models.DateField()),
                ('found_date', models.DateField()),
                ('company', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('source', models.CharField(max_length=100)),
                ('link', models.CharField(max_length=200)),
                ('topics', models.ManyToManyField(to='signup_app.Topic')),
            ],
        ),
    ]
