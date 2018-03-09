"""
Definition of models.
"""
import datetime
from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class ListItem(models.Model):
    name = models.CharField(max_length=280) #task to be completed
    complete = models.BooleanField(default=False) #whether task is complete or not
    goal_date = models.DateTimeField('goal completion date') #when task should be completed by
    user = models.ForeignKey(User, on_delete=models.CASCADE) #tie to user table so user's only see their own tasks
    def __str__(self):
        return self.name
