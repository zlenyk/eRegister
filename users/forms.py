from django import forms
from django.contrib.auth.forms import UserCreationForm
from users.models import UserProfile

class RegisterForm(UserCreationForm):
	username = forms.CharField(max_length=100, required=True)
	first_name = forms.CharField(max_length=100, required=True)
	last_name = forms.CharField(max_length=100, required=True)

	def save_user(self):
		return UserProfile.create_user(self)
