# Generated by Django 4.2.5 on 2023-10-04 09:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('guests', models.IntegerField()),
                ('attendance', models.CharField(max_length=20)),
                ('rsvp_date', models.DateTimeField(default=datetime.datetime.utcnow)),
            ],
        ),
    ]
