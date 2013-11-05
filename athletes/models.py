from django.db import models
from django.contrib.auth.models import User

class Athlete(models.Model):
    user = models.OneToOneField(User)
    date_of_birth = models.DateTimeField('Date')
    weight = models.PositiveSmallIntegerField()
    
    def __str__(self):
        return self.name

User.athlete = property(lambda u: Athlete.objects.get_or_create(user=u)[0])