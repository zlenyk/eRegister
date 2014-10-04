from django.forms import ModelForm
from school.models import Student,Group
from django.core.exceptions import ValidationError
class CreateStudentForm(ModelForm):
	class Meta:
		model = Student
		fields = ['first_name','last_name']

	def retrieve_student(self):
		first_name = self.cleaned_data.get('first_name')
		last_name = self.cleaned_data.get('last_name')
		return Student.get_student_by_name(first_name,last_name)

####################
class SearchStudentForm(ModelForm):
	class Meta:
		model = Student
		fields = ['first_name','last_name']
	
	def clean(self):
		first_name = self.cleaned_data.get('first_name')
		last_name = self.cleaned_data.get('last_name')
		student = Student.get_student_by_name(first_name,last_name)
		if student == None:
			raise ValidationError('')
		return self.cleaned_data
	
	def retrieve_student(self):
		first_name = self.cleaned_data.get('first_name')
		last_name = self.cleaned_data.get('last_name')
		return Student.get_student_by_name(first_name,last_name)
###################

class CreateGroupForm(ModelForm):
	class Meta:
		model = Group
		fields = ['name','lector','students']
#################
class SearchGroupForm(ModelForm):
	class Meta:
		model = Group
		fields = ['name']
		
	def clean(self):
		name = self.cleaned_data.get('name')
		group = Group.get_group_by_name(name)
		if group == None:
			raise ValidationError('')
		return self.cleaned_data
	
	def retrieve_group(self):
		name = self.cleaned_data.get('name')
		return Group.get_group_by_name(name)
#################
