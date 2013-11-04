from django.contrib import admin
from workouts.models import Workout

class WorkoutAdmin(admin.ModelAdmin):
    fields = [('date'),('duration'),('distance'),('description'),('type')]
    #inlines = [ChoiceInline]
    list_display = ('date', 'duration','distance', 'description','type')
    list_filter = ['date']
    search_fields = ['description']
    date_hierarchy = 'date'

admin.site.register(Workout, WorkoutAdmin)