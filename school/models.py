from django.db import models

class Student(models.Model):
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	@staticmethod
	def exist(f,l):
		return Student.objects.filter(first_name=f,last_name=l).count() != 0

	@staticmethod
	def get_by_name(f,l):
		if not Student.exist(f,l):
			return None
		return Student.objects.get(first_name=f,last_name=l)

	@staticmethod
	def get_student_by_id(id):
		return Student.objects.get(id=id)

	def __unicode__(self):
		return self.first_name + ' ' + self.last_name

####################Lector##########################
class Lector(models.Model):
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)

	@staticmethod
	def exist(f,l):
		return Lector.objects.filter(first_name=f,last_name=l).count() != 0

	@staticmethod
	def get_by_name(f,l):
		if not Lector.exist(f,l):
			return None
		return Lector.objects.get(first_name=f,last_name=l)

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
	def get_by_name(name):
		if not Group.group_exists(name):
			return None
		return Group.objects.get(name=name)

	@staticmethod
	def get_group_by_id(id):
		if not Group.group_id_exists(id):
			return None
		return Group.objects.get(id=id)

	def get_name(self):
		return self.name

	def get_lector(self):
		return self.lector

	def __unicode__(self):
		return self.name
