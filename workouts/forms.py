from django.forms import ModelForm
from models import Workout
from django import forms
from django.db import models

class WorkoutForm(ModelForm):
    description = forms.CharField(max_length=128, help_text="Please enter the description.")
    distance = forms.CharField(max_length=128, help_text="Please enter the distance.")
    date = forms.DateField(help_text="Wanneer heb je de training uitgevoerd?")
    #type
    class Meta:
        model = Workout
        fields = ['description', 'distance', 'type', 'date','duration']
        
        
        
        #http://stackoverflow.com/questions/10205657/django-modelform-create-or-update