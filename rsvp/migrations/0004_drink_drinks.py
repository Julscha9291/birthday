# Generated by Django 4.2.5 on 2023-10-05 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rsvp', '0003_remove_guest_drinks'),
    ]

    operations = [
        migrations.AddField(
            model_name='drink',
            name='drinks',
            field=models.ManyToManyField(blank=True, choices=[('Bier', 'Bier'), ('Sekt', 'Sekt'), ('Wein', 'Wein'), ('Aperol', 'Aperol'), ('Limo', 'Limo'), ('Cola', 'Cola')], to='rsvp.drink', verbose_name='Getränke'),
        ),
    ]
