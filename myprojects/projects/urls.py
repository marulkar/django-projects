from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^all/$', 'projects.views.All'),
	url(r'^get/(?P<projects_id>\d+)/$', 'projects.views.Project'),
	)
	