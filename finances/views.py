from django.shortcuts import render
from django.http import HttpResponseRedirect
from datetime import datetime
from school.forms import *
from school import views as school_views

def add_payment_page(request):
	return render(request,"finances/add_payment.html")

def add_payment(request):
	if request.method == 'POST':
		date_as_string = request.POST['date']
		date = datetime.strptime(date_as_string,"%d.%m.%Y")
		amount = request.POST['amount']
		student_id = request.POST['student_id']
		return HttpResponseRedirect('/home/')
	else:
		return HttpResponseRedirect('/finances/search_student_for_payment/')
