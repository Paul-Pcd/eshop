from django.db import models
from users.models import UserProfile
from shop.models import GoodsInfo


# Create your models here.
class ShopCart(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name='购买用户')
    goods_info = models.ForeignKey(GoodsInfo, verbose_name='购买商品')
    count = models.IntegerField('购买数量')
    create_date_time = models.DateTimeField(auto_now=True, verbose_name='购买时间')

    class Meta:
        verbose_name = '购物车'
        verbose_name_plural = verbose_name
        ordering = ('-create_date_time',)

    def __str__(self):
        return str(self.goods_info)
