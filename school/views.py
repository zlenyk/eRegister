from django.shortcuts import render
from django.http import HttpResponseRedirect
from school.forms import *
from school.models import Group,Student
from django.core.urlresolvers import reverse

def create_group(request):
	if request.method == 'POST':
		group_form = CreateGroupForm(request.POST)
		if group_form.is_valid():
			group_form.save()
			return HttpResponseRedirect('/home/')
	else:
		group_form = CreateGroupForm()
		return render(request, 'school/create_group.html',{'form':group_form})

def create_student(request):
	if request.method == 'POST':
		student_form = CreateStudentForm(request.POST)
		if student_form.is_valid():
			student_form.save()
			return HttpResponseRedirect('/home/')
		else:
			return render(request, 'school/create_student.html',{'error':True,'form':student_form})
	else:
		student_form = CreateStudentForm()
		return render(request, 'school/create_student.html',{'error':False,'form':student_form})

def search_group_module(request,url):
	group = None
	error = False
	if request.method == 'POST':
		group_form = SearchGroupForm(request.POST)
		if group_form.is_valid():
			group = group_form.retrieve_group()
			if group == None:
				error = True
		else:
			error = True
	return render(request,url,{'error':error,'form':SearchGroupForm(),'group':group})

def search_student_module(request,url):
	student = None
	error = False
	if request.method == 'POST':
		student_form = SearchStudentForm(request.POST)
		if student_form.is_valid():
			student = student_form.retrieve_student()
			if student == None:
				error = True
		else:
			error = True
	return render(request,url,{'error':error,'form':SearchStudentForm,'student':student})

def search_lector_module(request,url):
	lector = None
	error = False
	if request.method == 'POST':
		lector_form = SearchLectorForm(request.POST)
		if lector_form.is_valid():
			lector = lector_form.retrieve_lector()
			if lector == None:
				error = True
		else:
			error = True
	return render(request,url,{'error':error,'form':SearchLectorForm,'lector':lector})
