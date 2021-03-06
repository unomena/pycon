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
    
    def __unicode__(self):
        return u'%s (%s)' % (self.name, self.email)


class SpeakerRegistration(models.Model):
    
    name = models.CharField(max_length=128)
    surname = models.CharField(max_length=128, null=True)
    email = models.EmailField()
    contact_number = models.CharField(max_length=16, null=True, blank=True)
    comments = models.TextField(null=True, blank=True)
    bio = models.TextField(null=True)
    photo = models.ImageField(upload_to='speaker-photos', null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    talk_title = models.CharField(max_length=128, null=True)
    talk_type = models.IntegerField(choices=constants.TALK_TYPES, null=True)
    talk_level = models.IntegerField(choices=constants.TALK_LEVELS, null=True)
    talk_category = models.CharField(max_length=64, null=True)
    talk_duration = models.CharField(max_length=32, null=True)
    talk_description = models.TextField(null=True)
    talk_abstract = models.TextField(null=True)
    talk_notes = models.TextField(null=True)
    
    
    def __unicode__(self):
        return u'%s (%s)' % (self.name, self.email)


def post_registartion_save(sender, template, instance, created, **kwargs):
    if created:
        send_mail('PyCon ZA 2012', template,
                  settings.DEFAULT_FROM_EMAIL,
                  [instance.email],
                  fail_silently=True)

ATTENDEE_EMAIL = """
Thank you for registering for PyCon ZA 2012.

You can pay by EFT to the bank account below:

  Account number: 9275706696
  Branch code: 632005
  Account name: PyCon Conference
  Bank: ABSA
  Reference: PyCon (plus attendee initials+last name)

For assistance with registration and payment please contact
Wendy Griffiths on +27 82 377 5913 or e-mail team@za.pycon.org.

Looking forward to seeing you in October!
""".strip()

SPEAKER_EMAIL = """
Thanks for showing your interest.
We'll get in touch shortly.
""".strip()

models.signals.post_save.connect(post_registartion_save,
                                 sender=AttendeeRegistration,
                                 template=ATTENDEE_EMAIL)
models.signals.post_save.connect(post_registartion_save,
                                 sender=SpeakerRegistration,
                                 template=SPEAKER_EMAIL)
