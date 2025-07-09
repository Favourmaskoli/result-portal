from django.contrib import admin
from typing import Set
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

admin.site.unregister(User)

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    def get_form(self, request, obj = None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        is_superuser = request.user.is_superuser
        disables_fields:Set[str] = set()
        if not is_superuser:
            # form.base_fields['username'].disabled = True
            disables_fields |= {
                'is_superuser',
                'username',
                'is_staff',
            }
        for field in disables_fields:
            if field in form.base_fields:
                form.base_fields[field].disabled = True
        return form
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    readonly_fields = ('last_login', 'date_joined')
