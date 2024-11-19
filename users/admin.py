from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from django.utils.html import format_html

CustomUser = get_user_model()

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'username', 'is_active', 'is_staff', 'is_superuser', 'start_date', 'colored_status')
    list_filter = ('is_active', 'is_staff', 'is_superuser', 'start_date')
    search_fields = ('email', 'username')
    ordering = ('-start_date',)
    
    # Define fieldsets for add/change forms
    fieldsets = (
        (None, {
            'fields': ('email', 'password')
        }),
        (_('Personal info'), {
            'fields': ('username',)
        }),
        (_('Permissions'), {
            'fields': (
                'is_active',
                'is_staff',
                'is_superuser',
                'groups',
                'user_permissions',
            ),
        }),
        (_('Important dates'), {
            'fields': ('start_date', 'last_login')
        }),
    )
    
    # Define fieldsets for add form (simpler than change form)
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email',
                'username',
                'password1',
                'password2',
                'is_staff',
                'is_active',
                'is_superuser'
            ),
        }),
    )
    
    readonly_fields = ('last_login',)
    filter_horizontal = ('groups', 'user_permissions',)

    def colored_status(self, obj):
        """Display colored status indicator"""
        if obj.is_active:
            color = "green"
            status = "Active"
        else:
            color = "red"
            status = "Inactive"
        return format_html(
            '<span style="color: {};">{}</span>',
            color,
            status
        )
    colored_status.short_description = 'Status'

    def save_model(self, request, obj, form, change):
        """Custom save method for admin"""
        if not change and not obj.password:  # If creating new user without password
            obj.set_password(form.cleaned_data.get('password1'))
        super().save_model(request, obj, form, change)

    class Media:
        css = {
            'all': ('admin/css/custom_admin.css',)
        }
        js = ('admin/js/custom_admin.js',)