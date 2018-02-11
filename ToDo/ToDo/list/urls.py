from django.conf.urls import url
from . import views

app_name = 'list'
urlpatterns = [

    url(r'^contact$', views.contact, name='contact'),
    url(r'^about', views.about, name='about'),
    url(r'^addform/$',views.addform, name='addform'),
    url(r'^add/$',views.add, name='add'),
    url(r'^viewlist/$',views.viewlist, name='viewlist'),
    url(r'^change_tasks/$',views.change_tasks, name='change_tasks'),
    url(r'^create_account/$',views.create_account, name='create_account'),
    url(r'^$', views.index, name='index'),
]
