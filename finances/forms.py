from django.forms import ModelForm
from finances.models import Income,Outcome
from django.core.exceptions import ValidationError

class AddPaymentForm(ModelForm):
	class Meta:
		model = Income
		fields = ['amount','date']
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
