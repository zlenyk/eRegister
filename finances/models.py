from django.db import models
from school.models import Student,Lector

class Income(models.Model):
	amount = models.IntegerField()
	date = models.DateField()
	student = models.ForeignKey(Student)

class OutCome(models.Model):
	amount = models.IntegerField()
	date = models.DateField()
	lector = models.ForeignKey(Lector)
