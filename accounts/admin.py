from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

admin.site.unregister(User)

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    def get_form(self, request, obj = None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        is_superuser = request.user.is_superuser
        disabled_fields:set[str] = set()
        if(not is_superuser and obj is not None and obj==request.user):
            # form.base_fields['username'].disabled = True
            disabled_fields |= {
                'is_superuser',
                'username',
                'is_staff',
                'user_permissions',
                'groups',
            }
        for field in disabled_fields:
            if field in form.base_fields:
                form.base_fields[field].disabled = True
        return form
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    readonly_fields = ('last_login', 'date_joined')
