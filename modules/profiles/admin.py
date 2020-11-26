from __future__ import unicode_literals
from django.contrib import admin
from .models import Profiles
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils.html import format_html

User = get_user_model()


class ProfileInline(admin.StackedInline):
    model = Profiles
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'


class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, )
    list_display = ('username', 'first_name', 'last_name', 'is_staff', 'is_superuser','is_active', 'get_country')

    def get_country(self, instance):
        return instance.profiles.country
    get_country.short_description = 'Country'

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
