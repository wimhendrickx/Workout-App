from django.db import models

# Create your models here.

import datetime
from django.utils import timezone
from workouttypes.models import WorkoutType

class Workout(models.Model):
    type = models.ForeignKey(WorkoutType)
    date = models.DateTimeField('Date')
    duration = models.TimeField(("Duration"), blank=True)
    distance = models.IntegerField()
    description = models.CharField(max_length=200)
    def __str__(self):
        return self.description
    admin_order_field = 'date'
