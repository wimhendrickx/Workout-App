from django.db import models

# Create your models here.

import datetime
from django.utils import timezone
from workouttypes.models import WorkoutType
from django.db.models import Sum

class Workout(models.Model):
    type = models.ForeignKey(WorkoutType)
    date = models.DateTimeField('Date')
    duration = models.TimeField(("Duration"), blank=True)
    distance = models.IntegerField()
    description = models.CharField(max_length=200)
    def __str__(self):
        return self.description
    admin_order_field = 'date'


class WorkoutsManager(models.Model):
    def get_total_distances_aggregated_by_month(self):
        today = datetime.datetime.now()
	current_year = today.year
	current_month = today.month
	last_month = current_month - 1
	distance_curr_month = Workout.objects.filter(date__year=current_year).filter(date__month=current_month).aggregate(Sum('distance'))['distance__sum']
	distance_prev_month = Workout.objects.filter(date__year=current_year).filter(date__month=last_month).aggregate(Sum('distance'))['distance__sum']
        return [{'name': str(current_month) + ' ({0})'.format(current_year), 'total_distance': distance_curr_month}, {'name': str(last_month) + ' ({0})'.format(current_year), 'total_distance': distance_prev_month}]

class AmountOfWorkoutsbyType(models.Model):
   pass
   #workout WorkoutType.objects.all()