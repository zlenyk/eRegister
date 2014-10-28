from django.shortcuts import render
from django.http import HttpResponseRedirect
from school.forms import *
from school.models import *
from django.core.urlresolvers import reverse
from school.conf import Constants,Errors
from school.student_views import *
from school.lector_views import *
from school.group_views import *
from school.payments_views import *


def show_student_page(request):
	return search_student_engine(request,Constants.SHOW_STUDENT_PAGE)

def show_lector_page(request):
	return search_lector_engine(request,Constants.SHOW_LECTOR_PAGE)

def show_group_page(request):
	return search_group_engine(request,Constants.SHOW_GROUP_PAGE)

def add_payment_page(request):
	return search_student_engine(request,Constants.ADD_PAYMENT_PAGE)



####################################3
def render_show_group_page(request,url,group):
	return render(request,url,{'group':group})
