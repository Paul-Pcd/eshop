from django.contrib import admin
from .models import UserProfile, EmailVerifyRecord
# Register your models here.
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    pass

@admin.register(EmailVerifyRecord)
class EmailVerifyRecord(admin.ModelAdmin):
    pass
