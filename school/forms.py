from django.forms import ModelForm
from school.models import Student,Group

class StudentForm(ModelForm):
	class Meta:
		model = Student
		fields = ['first_name','last_name']
	
class GroupForm(ModelForm):
	class Meta:
		model = Group
		fields = ['name','lector','students']
