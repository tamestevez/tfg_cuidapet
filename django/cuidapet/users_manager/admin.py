from django.contrib import admin
from django.contrib.auth.models import Group

from .models import BaseUser

# Register your models here.


class BaseUserAdmin(admin.ModelAdmin):
    fieldsets = [
        (
            None,
            {
                "fields": [
                    "name",
                    "surnames",
                    "phone_number",
                    "email",
                    "password",
                    "address",
                    "town",
                    "role",
                    "token_password",
                ]
            },
        )
    ]


admin.site.register(BaseUser, BaseUserAdmin)
admin.site.unregister(Group)
