# accounts/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = [
        ('프로필', {'fields': ('username', 'password')}),
        ('개인정보', {'fields': ('nickname', 'email', 'profile_img', 'introduce')}),
        ('권한', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('로그인정보', {'fields': ('last_login', 'date_joined')}),
    ]
