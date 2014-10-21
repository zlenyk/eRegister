from django.shortcuts import render
from django.http import HttpResponseRedirect
from school.forms import *
from school import views as school_views
def add_payment(request):
	if request.method == 'POST':
		# do something with student payment. In post: student.id, date, amount
		pass
	else:
		return HttpResponseRedirect('/finances/search_student_for_payment/')
