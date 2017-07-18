from django.contrib import admin
from .models import OrderMain, OrderDetail
# Register your models here.
@admin.register(OrderMain)
class OrderMainAdmin(admin.ModelAdmin):
    list_display = ['id', 'order_id', 'user', 'is_pay', 'order_time', 'total', 'pay_time']


@admin.register(OrderDetail)
class OrderDetailAdmin(admin.ModelAdmin):
    list_display = ['id', 'goods_info', 'goods_price', 'count']
