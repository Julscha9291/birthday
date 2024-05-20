# Create your models here.
from django.db import models
from datetime import datetime

class Drink(models.Model):
    name = models.CharField(max_length=50)
    
    DRINK_CHOICES = [
        ('Bier', 'Bier'),
        ('Sekt', 'Sekt'),
        ('Wein', 'Wein'),
        ('Aperol', 'Aperol'),
        ('Limo', 'Limo'),
        ('Cola', 'Cola'),
    ]

    def __str__(self):
        return self.drinks
    
    class Meta:
        app_label = 'rsvp'

class Guest(models.Model):
    name = models.CharField(max_length=80)
    attendance = models.CharField(max_length=20)
    rsvp_date = models.DateTimeField(auto_now_add=True)
    drinks = models.ManyToManyField('Drink', blank=True, verbose_name='Getränke')

    def __str__(self):
        return self.name

    def total_guests(self):
        return self.guests

    def total_attending(self):
        if self.attendance == 'Ich nehme teil':
            return self.guests
        else:
            return 0

    def total_not_attending(self):
        if self.attendance == 'Ich nehme nicht teil':
            return self.guests
        else:
            return 0

        


  
