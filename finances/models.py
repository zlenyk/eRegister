from django.db import models
import os
from school.models import Student

class Income(models.Model):
	amount = models.IntegerField()
	date = models.DateField()
	title = models.CharField(max_length=100)
	student = models.ForeignKey(Student)
	@staticmethod
	def get_student_incomes(student):
		return Income.objects.filter(student = student)
	
	def __unicode__(self):
		return self.title + os.linesep + str(self.amount) + os.linesep + str(self.date)


class Outcome(models.Model):
	amount = models.IntegerField()
	date = models.DateField()
	title = models.CharField(max_length=100)
	lector_id = models.IntegerField()
