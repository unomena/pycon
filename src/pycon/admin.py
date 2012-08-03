from django.contrib import admin
from pycon.models import AttendeeRegistration, SpeakerRegistration

#==============================================================================
class AttendeeRegistrationAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'registration_type', 'timestamp')
    search_fields = ('name', 'surname')
    
admin.site.register(AttendeeRegistration, AttendeeRegistrationAdmin)

#==============================================================================
class SpeakerRegistrationAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'timestamp')
    search_fields = ('name', 'surname')
    
admin.site.register(SpeakerRegistration, SpeakerRegistrationAdmin)    