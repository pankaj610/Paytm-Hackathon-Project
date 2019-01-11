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


admin.site.register(Hospital, HospitalAdmin)

admin.site.register(Doctor, DoctorAdmin)
