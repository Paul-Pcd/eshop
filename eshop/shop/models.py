from django.db import models

from tinymce.models import HTMLField


# Create your models here.
class GoodsCategory(models.Model):
    category_name = models.CharField(max_length=20, verbose_name="商品分类")
    is_delete = models.BooleanField(default=0, verbose_name="是否删除")

    class Meta:
        verbose_name = '商品分类'
        verbose_name_plural = verbose_name
        ordering = ('id',)

    def __str__(self):
        return self.category_name


class GoodsArea(models.Model):
    city_name = models.CharField(max_length=20, verbose_name='商品产地')

    class Meta:
        verbose_name = '商品产地'
        verbose_name_plural = verbose_name
        ordering = ('id',)

    def __str__(self):
        return self.city_name


class GoodsInfo(models.Model):
    goods_name = models.CharField(max_length=30, verbose_name='商品名称')
    goods_images = models.ImageField(upload_to='goods/%Y/%m/%d', verbose_name='商品图片地址')
    goods_price = models.DecimalField(max_digits=5, decimal_places=2)
    goods_click = models.IntegerField(verbose_name='商品点击量')
    goods_unit = models.CharField(max_length=10, verbose_name='商品单位')
    is_delete = models.BooleanField(default=0, verbose_name='是否删除')
    goods_desc = models.TextField(verbose_name='商品描述')
    goods_stock = models.IntegerField(default=100, verbose_name='商品库存')
    goods_detail = HTMLField()
    goods_category = models.ForeignKey('GoodsCategory', verbose_name='商品分类')
    goods_city = models.ForeignKey('GoodsArea', verbose_name='商品产地', null=True)

    class Meta:
        verbose_name = '商品信息'
        verbose_name_plural = verbose_name
        ordering = ('id',)

    def __str__(self):
        return self.goods_name
