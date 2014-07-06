from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', TemplateView.as_view(template_name = 'index.html')),
    url(r'^home/', TemplateView.as_view(template_name = 'index.html')),
    url(r'^users/', include('users.urls')),
    url(r'^school/', include('school.urls')),
    
	# url(r'^eRegister/', include('eRegister.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

from django.contrib.auth.models import Group,Permission
from django.contrib.contenttypes.models import ContentType

lectors, p = Group.objects.get_or_create(name='Lectors')
moderators, p = Group.objects.get_or_create(name='Moderators')

content_type = ContentType.objects.get(app_label='users',model='userprofile')

is_lector, p = Permission.objects.get_or_create(codename='is_lector',name='Is User a Lector',content_type=content_type)
if p == True:
	lectors.permissions.add(is_lector)

is_moderator, p = Permission.objects.get_or_create(codename='is_moderator',name='Is User a Moderator',content_type=content_type)
if p == True:
	moderators.permissions.add(is_moderator)
