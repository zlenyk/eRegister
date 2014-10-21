from django.db import models

class Income(models.Model):
	amount = models.IntegerField()
	date = models.DateField()
	title = models.CharField(max_length=100)
	student_id = models.IntegerField()
	@staticmethod
	def get_student_incomes(id):
		return Income.objects.filter(student_id = id)


class Outcome(models.Model):
	amount = models.IntegerField()
	date = models.DateField()
	title = models.CharField(max_length=100)
	lector_id = models.IntegerField()
