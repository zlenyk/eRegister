from django.shortcuts import render
from django.http import HttpResponseRedirect
from school.forms import StudentForm,GroupForm
from school.models import Group
def add_group(request):
	if request.method == 'POST':
		group_form = GroupForm(request.POST)
		if group_form.is_valid():
			group_form.save_group()
			return HttpResponseRedirect('/home/')
	else:
		group_form = GroupForm()
		return render(request, 'school/add_group.html',{'form':group_form})

def add_student(request):
	if request.method == 'POST':
		student_form = StudentForm(request.POST)
		if student_form.is_valid():
			student_form.save_student()
			return HttpResponseRedirect('/home/')
	else:
		student_form = StudentForm()
		return render(request, 'school/add_student.html',{'form':student_form})

def show_group(request,group):
	return render(request,'school/show_group.html',{'group':group})

def search_group(request):
	if request.method == 'POST':
		name = request.POST['name']
		group = Group.get_group_by_name(name)
		if group == None:
			return render(request,'school/search_group.html',{'error':True})
		else:
			return render(request, 'school/show_group.html',{'group':group})
	else:
		return render(request,'school/search_group.html',{'error':False})

def manage_groups(request):
	return HttpResponseRedirect('/home/')
