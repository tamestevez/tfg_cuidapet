from django.contrib import admin
from .models import InsurancePolice

# Register your models here.

class InsurancePoliceAdmin(admin.ModelAdmin):
   pass

admin.site.register(InsurancePolice, InsurancePoliceAdmin)