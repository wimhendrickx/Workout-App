from django.contrib import admin
from workouttypes.models import WorkoutType

class WorkoutTypeAdmin(admin.ModelAdmin):
    fields = [('name')]
    #inlines = [ChoiceInline]
    list_display = ('name',)
    list_filter = ['name']
    search_fields = ['name']
    #date_hierarchy = 'date'

admin.site.register(WorkoutType, WorkoutTypeAdmin)