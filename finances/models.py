from django.db import models
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
		s = self.title + '\n' + self.amount + '\n' + self.date
		return smart_text(s,encoding='utf-8', strings_only=False, errors='strict')


class Outcome(models.Model):
	amount = models.IntegerField()
	date = models.DateField()
	title = models.CharField(max_length=100)
	lector_id = models.IntegerField()
