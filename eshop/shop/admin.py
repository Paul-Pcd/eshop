from django.contrib import admin
from .models import GoodsCategory, GoodsArea, GoodsInfo
# Register your models here.
@admin.register(GoodsCategory)
class GoodsCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'category_name', 'is_delete']

@admin.register(GoodsArea)
class GoodArea(admin.ModelAdmin):
    list_display = ['id', 'city_name']

@admin.register(GoodsInfo)
class GoodsInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'goods_name', 'goods_price', 'goods_click', 'goods_unit', 'goods_stock', 'goods_category', 'goods_city']
    list_per_page = 20
