from django import forms
from models import Athlete

class AthleteForm(forms.ModelForm):
    class Meta:
        model = Athlete
        fields = ('date_of_birth','weight')