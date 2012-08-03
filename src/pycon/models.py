'''
Created on 29 Jun 2012

@author: euan
'''
from django.db import models
from django.conf import settings
from django.core.mail import send_mail

from pycon import constants

class AttendeeRegistration(models.Model):
    
    name = models.CharField(max_length=128)
    surname = models.CharField(max_length=128, null=True)
    email = models.EmailField()
    contact_number = models.CharField(max_length=16, null=True, blank=True)
    registration_type = models.IntegerField(choices=constants.REGISTRATION_TYPES, null=True)
    comments = models.TextField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return '%s (%s)' % (self.name, self.email)


class SpeakerRegistration(models.Model):
    
    name = models.CharField(max_length=128)
    email = models.EmailField()
    comments = models.TextField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return '%s (%s)' % (self.name, self.email)
    
    
def post_registartion_save(sender, instance, created, **kwargs):
    if created:
        send_mail('PyCon ZA 2012', 
                  'Thanks for showing your interest.  We\'ll get in touch shortly',
                  settings.DEFAULT_FROM_EMAIL,
                  [instance.email], 
                  fail_silently=True)

models.signals.post_save.connect(post_registartion_save, sender=AttendeeRegistration)
models.signals.post_save.connect(post_registartion_save, sender=SpeakerRegistration)