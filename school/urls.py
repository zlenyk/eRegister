from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from school import views

urlpatterns = patterns('',
    url(r'^create_group/', views.create_group),
    url(r'^create_student/', views.create_student),
    url(r'^search_group/', views.search_group),
    url(r'^search_student/', views.search_student),
    url(r'^search_lector/', views.search_lector),
    url(r'^search_group_page/', views.search_group_page),
    url(r'^search_student_page/', views.search_student_page),
    url(r'^search_lector_page/', views.search_lector_page),
    #url(r'^add_student_to_group/', views.add_student_to_group),
    url(r'^add_payment/',views.add_payment),
    url(r'^add_payment_page/',views.add_payment_page),
    url(r'^search_student_for_payment/',views.search_student),
	)
