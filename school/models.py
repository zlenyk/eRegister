from django.db import models

class Student(models.Model):
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)

	@staticmethod
	def student_exists(first_name,last_name):
		return Student.objects.filter(first_name=first_name,last_name=last_name).count() != 0

	@staticmethod
	def create_student(student_form):
		first = student_form.cleaned_data['first_name']
		last = student_form.cleaned_data['last_name']	
		if not Student.student_exists(first,last):
			Student(first_name=first,last_name=last).save()
		return Student.objects.get(first_name=first,last_name=last)

	def __unicode__(self):
		return self.first_name + ' ' + self.last_name

####################Lector##########################
class Lector(models.Model):
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)

	def __unicode__(self):
		return self.first_name + ' ' + self.last_name

###################Group##############################
class Group(models.Model):
	name = models.CharField(max_length=150,unique=True)
	lector = models.ForeignKey(Lector,null=True,default=None,blank=True)
	students = models.ManyToManyField(Student)

	@staticmethod
	def group_exists(name):
		return Group.objects.filter(name=name).count() != 0

	@staticmethod 
	def create_group(group_form):
		name = group_form.cleaned_data['name']
		if not Group.group_exists(name):
			Group(name=name).save()
		return Group.objects.get(name=name)
	
	def __unicode__(self):
		return self.name
