'''
Created on 29 Jun 2012

@author: euan
'''
from django.db import models

class AttendeeRegistration(models.Model):
    
    name = models.CharField(max_length=128)
    email = models.EmailField()
    comments = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

class SpeakerRegistration(models.Model):
    
    name = models.CharField(max_length=128)
    email = models.EmailField()
    comments = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)