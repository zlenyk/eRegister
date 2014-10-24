from django.shortcuts import render
from django.http import HttpResponseRedirect
from datetime import datetime
from school.forms import *
from school.models import Student
from finances.forms import *

def add_payment_page(request):
	return render(request,"finances/add_payment_page.html",{'form':SearchStudentForm,'student':None,'error':False})

def add_payment(request):
	if request.method == 'POST':
		date_as_string = request.POST['date']
		date = datetime.strptime(date_as_string,"%d.%m.%Y")
		amount = request.POST['amount']
		title = request.POST['title']
		student_id = request.POST['student_id']
		student = Student.get_student_by_id(student_id)
		income = Income(date = date,amount=amount,student=student,title=title)
		form = AddPaymentForm(instance=income)
		if form.is_valid():
			form.save()
		else:
			return render(request,"finances/add_payment_page.html",{'form':SearchStudentForm,'student':None,'error':True})
			
		return HttpResponseRedirect('/home/')
