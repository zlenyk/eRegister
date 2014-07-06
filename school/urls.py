from django.conf.urls import patterns, url
from school import views

urlpatterns = patterns('',
    url(r'^add_group/', views.add_group),
    url(r'^add_student/', views.add_student),
	)
