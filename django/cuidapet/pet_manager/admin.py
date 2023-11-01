from django.contrib import admin
from .models import Animal, Passport, Marking, DeathRecord

class PassportInline(admin.StackedInline):
    model=Passport
    extra=1
    max_num=1

class MarkingInline(admin.StackedInline):
    model=Marking
    extra=1
    max_num=1

class DeathRecordInline(admin.StackedInline):
    model=DeathRecord
    max_num=1

class AnimalAdmin(admin.ModelAdmin):
    inlines=[
        MarkingInline,
        PassportInline,
        DeathRecordInline,
        ]

admin.site.register(Animal, AnimalAdmin)
