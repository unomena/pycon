'''
Created on 29 Jun 2012

@author: euan
'''
from django.conf.urls.defaults import patterns, include, url
from django.views import generic as generic_views
from django.views.generic import simple as simple_views

from pycon import forms

urlpatterns = patterns('',

    url(r'^$',
        simple_views.direct_to_template, 
        {'template' : 'pycon/index.html'}, 
        name='index'),
                       
    url(r'^index.html$',
        simple_views.redirect_to, 
        {'url' : '/'}, 
        name='index_redirect'),
                       
    url(r'^about.html$',
        simple_views.direct_to_template, 
        {'template' : 'pycon/about.html'}, 
        name='about'),
                       
    url(r'^venue.html$',
        simple_views.direct_to_template, 
        {'template' : 'pycon/venue.html'}, 
        name='venue'),
                       
    url(r'^location.html$',
        simple_views.direct_to_template, 
        {'template' : 'pycon/location.html'}, 
        name='location'),
                       
    url(r'^schedule.html$',
        simple_views.direct_to_template, 
        {'template' : 'pycon/schedule.html'}, 
        name='schedule'),
                       
    url(r'^sponsors.html$',
        simple_views.direct_to_template, 
        {'template' : 'pycon/sponsors.html'}, 
        name='sponsors'),
                       
    url(r'^sponsors_packages.html$',
        simple_views.direct_to_template, 
        {'template' : 'pycon/sponsors_packages.html'}, 
        name='sponsors_packages'),
                       
    url(r'^contact.html$',
        simple_views.direct_to_template, 
        {'template' : 'pycon/contact.html'}, 
        name='contact'),
                       
    url(r'^register.html$',
        generic_views.CreateView.as_view(form_class=forms.AttendeeRegistrationForm,
                                         template_name='pycon/register.html',
                                         success_url='/register_thanks.html'),
        name='register'),
                       
    url(r'^register_thanks.html$',
        simple_views.direct_to_template, 
        {'template' : 'pycon/register_thanks.html'}, 
        name='register_thanks'),
                       
    url(r'^speaker.html$',
        generic_views.CreateView.as_view(form_class=forms.SpeakerRegistrationForm,
                                         template_name='pycon/speaker.html',
                                         success_url='/speaker_thanks.html'),
        name='speaker'),
                       
    url(r'^speaker_thanks.html$',
        simple_views.direct_to_template, 
        {'template' : 'pycon/speaker_thanks.html'}, 
        name='speaker_thanks'),

# Old URL's

#    url(r'^register/attendee/$',
#        generic_views.CreateView.as_view(model=models.AttendeeRegistration,
#                                         template_name='pycon/popups/attendee.html',
#                                         success_url='/register/attendee/thanks/'),
#        name='register_attendee'),
#
#    url(r'^register/speaker/$',
#        
#        generic_views.CreateView.as_view(model=models.SpeakerRegistration,
#                                         template_name='pycon/popups/speaker.html',
#                                         success_url='/register/speaker/thanks/'),
#        name='register_speaker'),
#                       
#    url(r'^register/attendee/thanks/$',
#        simple_views.direct_to_template, 
#        {'template' : 'pycon/popups/attendee_thanks.html'}, 
#        name='attendee_thanks'),
#                       
#    url(r'^register/speaker/thanks/$',
#        simple_views.direct_to_template, 
#        {'template' : 'pycon/popups/speaker_thanks.html'}, 
#        name='speaker_thanks'),

)