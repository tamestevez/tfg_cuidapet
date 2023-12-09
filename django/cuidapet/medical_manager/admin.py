from django.contrib import admin

from .models import Disease, MedicalHistory, Surgery, Treatment, Vaccine


# Register your models here.
class VaccineInline(admin.StackedInline):
    model = Vaccine
    extra = 0


class DiseaseInline(admin.StackedInline):
    model = Disease
    extra = 0


class SurgeryInline(admin.StackedInline):
    model = Surgery
    extra = 0


class TreatmentInline(admin.StackedInline):
    model = Treatment
    extra = 0


class MedicalHistoryAdmin(admin.ModelAdmin):
    inlines = [
        VaccineInline,
        TreatmentInline,
        DiseaseInline,
        SurgeryInline,
    ]


admin.site.register(MedicalHistory, MedicalHistoryAdmin)
