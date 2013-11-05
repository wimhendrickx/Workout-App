from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^edit/$', athletes.views.edit),
)