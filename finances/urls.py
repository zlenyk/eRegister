from django.conf.urls import patterns, url
from finances import views
import school

urlpatterns = patterns('',
	url(r'^add_payment/',views.add_payment),
	url(r'^add_payment_page/',views.add_payment_page),
	url(r'^search_student_for_payment/',school.views.search_student)
	)
