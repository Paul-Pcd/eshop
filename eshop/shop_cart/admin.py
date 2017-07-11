from django.contrib import admin
from .models import ShopCart
# Register your models here.
@admin.register(ShopCart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['id', 'goods_info', 'user', 'count', 'create_date_time']
