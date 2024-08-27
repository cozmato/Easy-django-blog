from django.contrib import admin
from . models import *
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

class UserAdmin(BaseUserAdmin):
    list_display = ("username", 'first_name', 'last_name', 'email', "is_active", "date_joined")
    search_fields = ("username", 'first_name', 'last_name', "email")
    filter_horizontal = ()
    fieldsets = ()
    list_filter = ['last_login']

    add_fieldsets = (
        (None, {
            'classes': ('wide'),
            'fields': ("username", "first_name", "last_name", "email",
                         'password1', 'password2'),
        }),
    )

    ordering = ['email']


admin.site.register(User, UserAdmin)
admin.site.register(EmailMsg)
admin.site.register(Product)
admin.site.register(ViewCount)
admin.site.register(Category)
