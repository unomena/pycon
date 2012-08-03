'''
Created on 29 Jun 2012

@author: euan
'''
from django.conf.urls.defaults import patterns, include, url
from django.views import generic as generic_views
from django.views.generic import simple as simple_views

from pycon import models

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