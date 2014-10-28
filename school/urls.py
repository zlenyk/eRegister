from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from school import views,group_views,student_views,lector_views

urlpatterns = patterns('',
    url(r'^show_group_page/', views.show_group_page),
    url(r'^show_student_page/', views.show_student_page),
    url(r'^show_lector_page/', views.show_lector_page),
#    url(r'^add_student_to_group/', student_views.add_student_to_group),
    url(r'^add_payment/',views.add_payment),
    url(r'^add_payment_page/',views.add_payment_page),
    url(r'^search_student_for_payment/',student_views.search_student),
    
	url(r'^search_student/', student_views.search_student),
    url(r'^search_group/', group_views.search_group),
	url(r'^search_lector/', lector_views.search_lector),
    
	url(r'^create_group/', group_views.create_group),
    url(r'^create_student/', student_views.create_student),
	)
