from django.forms import ModelForm
from school.models import Student

class StudentForm(ModelForm):
	class Meta:
		model = Student
		fields = ['first_name','last_name']
	
	def	save_student(self):
		return Student.create_student(self)
