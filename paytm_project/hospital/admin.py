from django.contrib import admin
from .models import *



class HospitalAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug':('name',)}


class DoctorAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'dob', 'address', 'available', 'description', 'phoneno']
    list_filter = ['available','dob']
    list_editable = ['available']
    prepopulated_fields = {'slug':('name',)}

class AmbulanceAdmin(admin.ModelAdmin):
    list_display = ['driver_name', 'slug', 'ambulance_no', 'phoneno', 'available']
    list_filter = ['available']
    list_editable = ['available']
    prepopulated_fields = {'slug':('driver_name',)}


admin.site.register(Hospital, HospitalAdmin)
admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Ambulance, AmbulanceAdmin)
