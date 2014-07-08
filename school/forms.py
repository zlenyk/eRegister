from django.forms import ModelForm
from school.models import Student,Group

class StudentForm(ModelForm):
	class Meta:
		model = Student
		fields = ['first_name','last_name']
	
	def	save_student(self):
		return Student.create_student(self)

class GroupForm(ModelForm):
	class Meta:
		model = Group
		fields = ['name','lector','students']

	def save_group(self):
		return Group.create_group(self)
