# users/admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import UserChangeForm
from .models import User

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User

class UserAdmin(BaseUserAdmin):
    form = CustomUserChangeForm
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'phone', 'profile_picture', 'is_verified', 'account_number', 'internal_revenew_required', 'home_address', 'country', 'gender', 'account_type', 'city', 'zipcode', 'pin', 'balance', 'is_banned', 'is_limit', 'date_of_birth')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'password1', 'password2'),
        }),
    )
    list_display = ('email', 'first_name', 'last_name', 'phone', 'is_staff')
    search_fields = ('email', 'first_name', 'last_name', 'phone')
    ordering = ('email',)

    def save_model(self, request, obj, form, change):
        # Ensure the password is hashed properly before saving
        if obj.pk is not None and 'password' in form.changed_data:
            obj.set_password(form.cleaned_data['password'])
        super().save_model(request, obj, form, change)

admin.site.register(User, UserAdmin)
