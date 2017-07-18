from django.contrib import admin
from .models import UserProfile, EmailVerifyRecord, Receiver
# Register your models here.


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'telephone_number', 'email', 'city', 'is_active', 'is_staff']


@admin.register(EmailVerifyRecord)
class EmailVerifyRecord(admin.ModelAdmin):
    list_display = ['id', 'email', 'code', 'send_type', 'send_date']


@admin.register(Receiver)
class ReceiverAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'city', 'telephone', 'address', 'user']

