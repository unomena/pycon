'''
Created on 29 Jun 2012

@author: euan
'''
from django.db import models
from django.conf import settings
from django.core.mail import send_mail

class AttendeeRegistration(models.Model):
    
    name = models.CharField(max_length=128)
    email = models.EmailField()
    comments = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return '%s (%s)' % (self.name, self.email)


class SpeakerRegistration(models.Model):
    
    name = models.CharField(max_length=128)
    email = models.EmailField()
    comments = models.TextField()
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