'''
Created on 20 Mar 2011

@author: euan
'''
from django.conf import settings
from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    (r'^', include('%s.urls' % settings.PROJECT_NAME)),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
        
)

#------------------------------------------------------------------------------
# Django serves media
if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$',
         'django.views.static.serve', 
         {'document_root' : settings.MEDIA_ROOT, 
          'show_indexes': True}
         ),
    )