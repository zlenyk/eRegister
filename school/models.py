from django.db import models

class Student(models.Model):
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)

	@staticmethod
	def student_exists(form):
		first = form.cleaned_data['first_name']
		last = form.cleaned_data['last_name']	
		return Student.objects.filter(first_name=first,last_name=last).count() != 0

	@staticmethod
	def get_student(form):
		if not student_exists(form):
			return None
		first = form.cleaned_data['first_name']
		last = form.cleaned_data['last_name']
		return Student.objects.get(first_name=first,last_name=last)

	def __unicode__(self):
		return self.first_name + ' ' + self.last_name

####################Lector##########################
class Lector(models.Model):
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)

	@staticmethod
	def create_lector(first,last):
		Lector(first_name=first,last_name=last).save()
		return Lector.objects.get(first_name=first,last_name=last)

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
	def group_id_exists(id):
		return Group.objects.filter(id=id).count() != 0

	@staticmethod
	def get_group_by_name(name):
		if Group.group_exists(name):
			return Group.objects.get(name=name)
		else:
			return None

	@staticmethod
	def get_group_by_id(id):
		if Group.group_id_exists(id):
			return Group.objects.get(id=id)
		else:
			return None

	@staticmethod 
	def create_group(group_form):
		name = group_form.cleaned_data['name']
		lector = group_form.cleaned_data['lector']
		if not Group.group_exists(name):
			Group(name=name,lector=lector).save()
		return Group.get_group_by_name(name)
	
	def get_name(self):
		return self.name
	
	def get_lector(self):
		return self.lector
	
	def __unicode__(self):
		return self.name
