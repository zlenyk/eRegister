from django.shortcuts import render
from django.http import HttpResponseRedirect
from school.forms import StudentForm,GroupForm
from school.models import Group
def create_group(request):
	if request.method == 'POST':
		group_form = GroupForm(request.POST)
		if group_form.is_valid():
			group_form.save()
			return HttpResponseRedirect('/home/')
	else:
		group_form = GroupForm()
		return render(request, 'school/create_group.html',{'form':group_form})

def create_student(request):
	if request.method == 'POST':
		student_form = StudentForm(request.POST)
		if student_form.is_valid():
			student_form.save()
			return HttpResponseRedirect('/home/')
	else:
		student_form = StudentForm()
		return render(request, 'school/create_student.html',{'form':student_form})

def add_student_to_group(request,group_id):
	if request.method == 'POST':
		student_form = StudentForm(request.POST)
		student = Student.get_student(student_form)
		if student == None:
			return render(request,'school/add_student.html',{'Error':True})


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
