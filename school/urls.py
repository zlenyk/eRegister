from django.conf.urls import patterns, url
from school import views

urlpatterns = patterns('',
    url(r'^add_group/', views.add_group),
    url(r'^add_student/', views.add_student),
    url(r'^manage_groups/', views.manage_groups),
    url(r'^search_group/', views.search_group),
	)
