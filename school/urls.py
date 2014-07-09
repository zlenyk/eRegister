from django.conf.urls import patterns, url
from school import views

urlpatterns = patterns('',
    url(r'^create_group/', views.create_group),
    url(r'^create_student/', views.create_student),
    url(r'^manage_groups/', views.manage_groups),
    url(r'^search_group/', views.search_group),
	)
