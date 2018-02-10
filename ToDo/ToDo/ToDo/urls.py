"""
Definition of urls for ToDo.
"""

from datetime import datetime
from django.conf.urls import include, url
from django.contrib.auth import views as auth_views
from django.contrib import admin

# Uncomment the next lines to enable the admin:


urlpatterns = [
    # Examples:
    url(r'^admin/', admin.site.urls, name='admin'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout$', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^list/', include('list.urls'), name='list'),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    url(r'',include('list.urls')),
]
