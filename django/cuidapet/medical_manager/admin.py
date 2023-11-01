from django.contrib import admin
from .models import MedicalHistory, Vacine, Treatment, Disease, Surgery

# Register your models here.
class VacineInline(admin.StackedInline):
    model=Vacine
    extra=0


class DiseaseInline(admin.StackedInline):
    model=Disease
    extra=0

class SurgeryInline(admin.StackedInline):
    model=Surgery
    extra=0

class TreatmentInline(admin.StackedInline):
    model=Treatment
    extra=0

class MedicalHistoryAdmin(admin.ModelAdmin):
    inlines=[
        VacineInline,
        TreatmentInline,
        DiseaseInline,
        SurgeryInline,
    ]

admin.site.register(MedicalHistory, MedicalHistoryAdmin)