from django.contrib import admin
from .models import *

# Register your models here.

class OfficerAdmin(admin.ModelAdmin):
    list_display = [ "get_name", "radio_id", "vehicle", "active_call", ]

class VehicleAdmin(admin.ModelAdmin):
    list_display = [ "verbal_name", "get_assignee", ]

    def get_assignee(self, obj):
        if (hasattr(obj, "officer")):
            return obj.officer
        else:
            return None 
    get_assignee.short_description = "Assignee"
    
admin.site.register(Officer, OfficerAdmin)
admin.site.register(Vehicle, VehicleAdmin)
admin.site.register(LicensePlate)
admin.site.register(Call)
