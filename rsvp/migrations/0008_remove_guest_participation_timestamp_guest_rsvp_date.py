# Generated by Django 4.2.5 on 2023-10-15 10:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rsvp', '0007_remove_guest_rsvp_date_guest_participation_timestamp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='guest',
            name='participation_timestamp',
        ),
        migrations.AddField(
            model_name='guest',
            name='rsvp_date',
            field=models.DateTimeField(default=datetime.datetime.utcnow),
        ),
    ]
