"""
Definition of views.
"""

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpRequest, JsonResponse, HttpResponse, HttpResponseRedirect
from django.core import serializers
from django.urls import reverse
from django.views import generic
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from datetime import datetime
from .models import ListItem

#home page where user can view, add, or edit tasks
@login_required
def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'list/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Brent Gruber',
            'message':'To Do List Web App',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )


#View which allows user to view their to  do list
@login_required
def viewlist(request):
    print(request.user)
    latest_list = ListItem.objects.filter(User=request.user).order_by('goal_date')
    context = {'latest_list': latest_list}
    return render(request, 'list/mytodolist.html', context)

#Allow users to mark their tasks complete or incomplete
@login_required
def change_tasks(request):
    full_list = ListItem.objects.filter(User=request.user)
    #loop through to do list
    for item in full_list:
        temp = str(item.pk)
        if temp in request.POST:
            item.complete = True
        else:
            item.complete = False
        item.save()
    return HttpResponseRedirect(reverse('list:viewlist'))

#load page to add a task
#TODO: replace with a card
@login_required
def addform(request):
    return render(request, 'list/add.html')

#Add the task item through POST
@login_required
def add(request):
    newLI = ListItem(name=request.POST['Name'], goal_date=request.POST['goal_date'],complete=False, User=request.user)
    newLI.save()
    return HttpResponseRedirect(reverse('list:index'))

#create a user account
def create_account(request):
    user = User.objects.create_user(username=request.POST['username'], email=request.POST['email'],password=request.POST['password'])
    login = authenticate(username=request.POST['username'], password=request.POST['password'])
    if login is not None:
        return HttpResponseRedirect(reverse('list:index'))
    else:
        return HttpResponseRedirect(reverse('login'))
