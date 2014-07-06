from django.db import models

class Student(models.Model):
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	id_number = models.IntegerField(default=0)

	def __unicode__(self):
		return self.name

class Lector(models.Model):
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	id_number = models.IntegerField(default=0)

	def __unicode__(self):
		return self.name

class Group(models.Model):
	id_number = models.IntegerField(default=0)
	lector = models.OneToOneField(Lector,primary_key=True)
	students = models.ManyToManyField(Student)
