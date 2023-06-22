from django.contrib import admin
from .models import *

# Register your models here.

class OfficerAdmin(admin.ModelAdmin):
    list_display = [ "get_name", "radio_id", "active_call" ]

admin.site.register(Officer, OfficerAdmin)
admin.site.register(Vehicle)
admin.site.register(LicensePlate)
admin.site.register(Call)
