from django.shortcuts import render
from django.http import HttpResponseRedirect
from datetime import datetime
from school.forms import *
from school.models import Student
from finances.forms import *
from utilities.models import Constants

def add_payment_page(request):
	return render(request,Constants.ADD_PAYMENT_PAGE,{'form':SearchStudentForm,'student':None,'error':False})

def add_payment(request):
	if request.method == 'POST':
		date_as_string = request.POST['date']
		date = datetime.strptime(date_as_string,"%d.%m.%Y").date()
		student_id = request.POST['student_id']
		student = Student.get_student_by_id(student_id)
		form = AddPaymentForm(request.POST)
		if form.is_valid():
			income = form.save(commit=False)
			income.student = student
			income.date = date
			income.save()
			return HttpResponseRedirect('/home/')
		else:
			return render(request,Constants.ADD_PAYMENT_PAGE,{'form':SearchStudentForm,'student':student,'error':True})		
	return HttpResponseRedirect('/home/')
