from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.forms import AuthenticationForm, SetPasswordForm
from users.forms import RegisterForm

def login(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect('/home/')

	login_form = AuthenticationForm()
	if request.method == 'POST':
		_username = request.POST['username']
		_password = request.POST['password']
		user = auth.authenticate(username=_username, password=_password)
		if user is not None and user.is_active:
			auth.login(request, user)
			context = {'auth': True}
			return HttpResponseRedirect('/home/')
		else:
			context = {'auth': False, 'form': login_form}
			return render(request, 'users/login.html', context)
	else:
		return render(request, 'users/login.html', {'form': login_form})

def logout(request):
	auth.logout(request)
	return HttpResponseRedirect('/home/')

#def register(request):
#	if request.user.is_authenticated():
#		return HttpResponseRedirect('/home/')
#
#	if request.method == 'POST':
#		register_form = RegisterForm(request.POST)
#		if register_form.is_valid():
#			register_form.save_user()
#			return HttpResponseRedirect('/home/')
#		else:
#			return render(request, 'users/register.html', {'form': RegisterForm(),'error':True})
#	else:
#		return render(request, 'users/register.html', {'form': RegisterForm()})
