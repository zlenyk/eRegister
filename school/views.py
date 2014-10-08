from django.shortcuts import render
from django.http import HttpResponseRedirect
from school.forms import *
from school.models import Group,Student

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

def show_group(request,group):
	return render(request,'school/show_group.html',{'group':group})

def search_group(request):
	if request.method == 'POST':
		group_form = SearchGroupForm(request.POST)
		if group_form.is_valid():
			group = group_form.retrieve_group()
			if group == None:
				return render(request,'school/search_group.html',{'error':True,'form':SearchGroupForm()})
			else:
				return show_group(request,group)
		else:
			return render(request,'school/search_group.html',{'error':True,'form':SearchGroupForm()})

	else:
		return render(request,'school/search_group.html',{'error':False,'form':SearchGroupForm()})

def show_student(request,student):
	return render(request,'school/show_student.html',{'student':student})

def search_student(request):
	if request.method == 'POST':
		student_form = SearchStudentForm(request.POST)
		if student_form.is_valid():
			student = student_form.retrieve_student()
			if student == None:
				return render(request,'school/search_student.html',{'error':True,'form':SearchStudentForm})
			else:
				return show_student(request,student)
		else:
			return render(request,'school/search_student.html',{'error':True,'form':SearchStudentForm})
	else:
		return render(request,'school/search_student.html',{'error':False,'form':SearchStudentForm})

def show_lector(request,lector):
	return render(request,'school/show_lector.html',{'lector':lector})

def search_lector(request):
	if request.method == 'POST':
		lector_form = SearchLectorForm(request.POST)
		if lector_form.is_valid():
			lector = lector_form.retrieve_lector()
			if lector == None:
				return render(request,'school/search_lector.html',{'error':True,'form':SearchLectorForm})
			else:
				return show_lector(request,lector)
		else:
			return render(request,'school/search_lector.html',{'error':True,'form':SearchLectorForm})
	else:
		return render(request,'school/search_lector.html',{'error':False,'form':SearchLectorForm})
