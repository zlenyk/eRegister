from django.shortcuts import render

def add_group(request):
	return render(request, 'school/add_group.html')

def add_student(request):
	return render(request, 'school/add_student.html')
