from allauth.account.models import EmailAddress
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username', 'first_name', 'last_name', 'email', 'taxpayer', ]
    fieldsets = (
        (None, {
            'fields': ('username', 'first_name', 'last_name', 'middle_name', 'email', 'taxpayer', 'is_staff')
        }),
    )


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.unregister(Group)
admin.site.unregister(EmailAddress)

admin.site.site_header = 'Модерация'
admin.site.index_title = 'Модерация'
admin.site.site_title = 'Модерация'
