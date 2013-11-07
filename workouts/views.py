# Create your views here.

from django.db.models import Sum

from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render, get_object_or_404, render_to_response
from django.core.urlresolvers import reverse
from django.http import Http404, HttpResponseRedirect
#from django.httpresponse import httpresponseredirect

from workouts.models import Workout
from workouts.models import WorkoutsManager
from workouttypes.models import WorkoutType
from workouts.forms import WorkoutForm

def index(request):
    latest_workout_list = Workout.objects.all().order_by('-date')[:30]
    wmanager = WorkoutsManager()
    months = wmanager.get_total_distances_aggregated_by_month()
    context = {'latest_workout_list': latest_workout_list, 'months': months}
    return render(request, 'workouts/index.html', context)
    
def detail(request, workout_id):
    workout = get_object_or_404(Workout, pk=workout_id)
    return render(request, 'workouts/detail.html', {'workout': workout})
    
def summary(request):
    for e in WorkoutType.objects.all(): #.filter(name='Fiets')
        s = Workout.objects.all().filter(type__name__exact=e.name).aggregate(Sum('distance'))
    return render(request, 'workouts/summary.html', {'summary_bike': s})

def add(request):
    
    # Get the context from the request.
    context = RequestContext(request)
    print request.method
    # A HTTP POST?
    if request.method == 'POST':
        print "hier"
        form = WorkoutForm(request.POST)

        # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new category to the database.
            form.save(commit=True)
            
            # Now call the index() view.
            # The user will be shown the homepage.
            return index(request)
        else:
            # The supplied form contained errors - just print them to the terminal.
            print form.errors
    else:
        # If the request was not a POST, display the form to enter details.
        form = WorkoutForm()

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    return render_to_response('workouts/add.html', {'form': form}, context)
    
def edit(request, id=None, template_name='workouts/edit.html'):
    workout = None
    if id!=None:
        workout = get_object_or_404(Workout, pk=id)
        print "ik krijg hier nen id binnen: {0}".format(id)
	print "voorvoor ik heb het object met id {0} opgehaald".format(workout.id)
        #if article.user != request.user:
        #    return HttpResponseForbidden()
    else:
        workout = Workout()
 
    if request.POST:
        form = WorkoutForm(request.POST, instance=workout)
        if form.is_valid():
	    print "achterachter ik heb het object met id {0} opgehaald".format(workout.id)
            print "hier ben ik nu: en ik ben bezig met instance: {0}".format(form.instance.id)
	    print "is de form bound?: {0}".format(form.is_bound)
            print workout
            form.save()
            # messages.add_message(request, messages.SUCCESS, _('Workout correctly saved.'))
            # If the save was successful, redirect to another page
            
            #redirect_url = reverse('index')
            return HttpResponseRedirect('../../')
            #return index(request)
    else:
        form = WorkoutForm(instance=workout)
 
    return render_to_response(template_name, {
        'form': form,
    }, context_instance=RequestContext(request))
