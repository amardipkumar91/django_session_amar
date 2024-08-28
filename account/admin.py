from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from account.models import *

# Register your models here.

class UserModelAdmin(BaseUserAdmin):
    list_display = ["id", "email", "name", "is_admin"]
    list_filter = ["is_admin"]
    fieldsets = [
        ("User Credentials", {"fields" : ["email", "password" ]}),
        ("Personal Info", {"fields" : ["name"]}),
        ("Permissions", {"fields" : ["is_admin"]})

    ]

    add_fieldsets = [
        (
            None, 
            {
                "classes" : ["wide"],
                "fields" : ["email", "name", "password1", "password2"]
            },
        )
    ]
    search_fields = ["email"]
    ordering = ["email", "id"]
    filter_horizontal = []
class EmployeeModelAdmin(admin.ModelAdmin):
    fields = ('name', 'salary', 'department')
    list_display = ('name', 'salary', 'department')


admin.site.register(User, UserModelAdmin)
admin.site.register(Employee, EmployeeModelAdmin)

