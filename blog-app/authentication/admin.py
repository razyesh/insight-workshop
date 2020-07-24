from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


# Register your models here.
class UserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (
            'Personal info',
            {
                'fields': (
                    'image', 'no_of_blog'
                )
            }
        ),
    )


admin.site.register(User, UserAdmin)
