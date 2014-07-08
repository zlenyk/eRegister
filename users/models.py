from django.db import models
from django.contrib.auth.models import User,UserManager,Group
from school.models import Lector

class UserProfile(User):

	objects = UserManager()

	@staticmethod
	def create_user(register_form):
		new_user = UserProfile.objects.create_user(username = register_form.cleaned_data['username'],
													password = register_form.cleaned_data['password1'],
													first_name = register_form.cleaned_data['first_name'],
													last_name = register_form.cleaned_data['last_name'],
													)
		new_user.save()
		
		group = Group.objects.get(name='Lectors')
		group.user_set.add(new_user)
		Lector.create_lector(register_form.cleaned_data['first_name'],
							register_form.cleaned_data['last_name']
							)
		return new_user

	@staticmethod
	def login_exists(login):
		if UserProfile.objects.filter(username=login):
			return True
		else:
			return False

	@staticmethod
	def get_user(login):
		if login_exists(login):
			return UserProfile.objects.get(username=login)
		else:
			return None

	def __unicode__(self):
		return self.username
