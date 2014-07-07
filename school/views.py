from django.shortcuts import render
from django.http import HttpResponseRedirect
from school.forms import StudentForm

def add_group(request):
	return render(request, 'school/add_group.html')

def add_student(request):
	if request.method == 'POST':
		student_form = StudentForm(request.POST)
		if student_form.is_valid():
			student_form.save_student()
			return HttpResponseRedirect('/home/')
	else:
		student_form = StudentForm()
		return render(request, 'school/add_student.html',{'form':student_form})
