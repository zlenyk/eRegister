from django.conf.urls import patterns, url
from school import views

urlpatterns = patterns('',
    url(r'^create_group/', views.create_group),
    url(r'^create_student/', views.create_student),
    url(r'^search_group/', views.search_group),
    url(r'^search_student/', views.search_student),
    url(r'^search_lector/', views.search_lector),
	)
