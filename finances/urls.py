from django.conf.urls import patterns, url
from finances import views
import school

urlpatterns = patterns('',
	url(r'^add_payment/',views.add_payment),
	url(r'^search_student_for_payment/',school.views.search_student_module,{'url':'finances/add_payment.html'})
	)
