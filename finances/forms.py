from django.forms import ModelForm
from finances.models import Income,Outcome
from django.core.exceptions import ValidationError

class AddPaymentForm(ModelForm):
	class Meta:
		model = Income
		fields = ['amount','date','student','title']
