from django.conf.urls import patterns, url

from workouts import views

urlpatterns = patterns('',
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    url(r'^(?P<workout_id>\d+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    # url(r'^(?P<workout_id>\d+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    # added the word 'specifics'
    url(r'^specifics/(?P<workout_id>\d+)/$', views.detail, name='detail'),
    url(r'^summary$', views.summary, name='summary'),
    url(r'^add/$', views.edit, {}, 'add'),
    url(r'^edit/(?P<id>\d+)/$', views.edit, {}, 'edit'),
    url(r'^edit/$', views.edit, {}, 'edit'),
)