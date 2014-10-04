from django import forms
from django.contrib.auth.forms import UserCreationForm
from users.models import UserProfile

class RegisterForm(UserCreationForm):
	first_name = forms.CharField(max_length=100, required=True)
	last_name = forms.CharField(max_length=100, required=True)

	def save_user(self):
		password = self.cleaned_data.get('password1')
		username = self.cleaned_data.get('username')
		first_name = self.cleaned_data.get('first_name')
		last_name = self.cleaned_data.get('last_name')
		return UserProfile.create_user(username,password,first_name,last_name)
