from django.shortcuts import render
from django.http import HttpResponseRedirect
from school.forms import *
from school.models import *
from django.core.urlresolvers import reverse
from school.conf import Constants,Errors
from datetime import datetime
#####################################

def create_group(request):
	if request.method == 'POST':
		group_form = CreateGroupForm(request.POST)
		if group_form.is_valid():
			group_form.save()
			return HttpResponseRedirect('/home/')
		else:
			return render(request,Constants.CREATE_GROUP_PAGE,{'error':True,'form':group_form})
	else:
		group_form = CreateGroupForm()
		return render(request, Constants.CREATE_GROUP_PAGE,{'error':False,'form':group_form})

def create_student(request):
	if request.method == 'POST':
		student_form = CreateStudentForm(request.POST)
		if student_form.is_valid():
			student_form.save()
			return HttpResponseRedirect('/home/')
		else:
			return render(request,Constants.CREATE_STUDENT_PAGE ,{'error':True,'form':student_form})
	else:
		student_form = CreateStudentForm()
		return render(request, Constants.CREATE_STUDENT_PAGE,{'error':False,'form':student_form})

#######################################

def search_group_page(request):
	return render(request,Constants.SEARCH_GROUP_PAGE,{'error':False,'form':SearchGroupForm,'group':None})

def search_student_page(request):
	return render(request,Constants.SEARCH_STUDENT_PAGE,{'error':False,'form':SearchStudentForm,'student':None})

def search_lector_page(request):
	return render(request,Constants.SEARCH_LECTOR_PAGE,{'error':False,'form':SearchLectorForm,'lector':None})

##################################

def search_group(request):
	group = None
	error = False
	if request.method == 'POST':
		url = request.POST.get('template_path',"");
		group_form = SearchGroupForm(request.POST)
		if group_form.is_valid():
			group = group_form.retrieve_group()
			if group == None:
				error = True
			else:
				return render_show_group_page(request,url,group)
		else:
			error = True
		return render(request,url,{'error':error,'form':SearchGroupForm,'group':group})
	#this should not happen
	return render(request,Constants.ERROR);

def search_student(request):
	student = None
	error = False
	if request.method == 'POST':
		url = request.POST.get('template_path',"");
		student_form = SearchStudentForm(request.POST)
		if student_form.is_valid():
			student = student_form.retrieve_student()
			if student == None:
				error = True
			else:
				return render_show_student_page(request,url,student)
		else:
			error = True
		return render(request,url,{'error':error,'form':SearchStudentForm,'student':student})
	#this should not happen
	return render(request,Constants.ERROR);

def search_lector(request):
	lector = None
	error = False
	if request.method == 'POST':
		url = request.POST.get('template_path',"");
		lector_form = SearchLectorForm(request.POST)
		if lector_form.is_valid():
			lector = lector_form.retrieve_lector()
			if lector == None:
				error = True
			else:
				return render_show_lector_page(request,url,lector)
		else:
			error = True
		return render(request,url,{'error':error,'form':SearchLectorForm,'lector':lector})
	#this should not happen
	return render(request,Constants.ERROR);

##############################################

def render_show_student_page(request,url,student):
	incomes = Income.get_student_incomes(student)
	return render(request,url,{'student':student,'incomes':incomes})

def render_show_group_page(request,url,group):
	return render(request,url,{'group':group})

def render_show_lector_page(request,url,lector):
	return render(request,url,{'lector':lector})

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
