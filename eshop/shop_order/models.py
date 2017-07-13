from django.db import models
from users.models import UserProfile
from shop.models import GoodsInfo


# Create your models here.
class OrderMain(models.Model):
    # 1 2 3 4
    orderid = models.CharField(max_length=20, primary_key=True, verbose_name='订单编号')  # 20170713000000用户id
    order_time = models.DateTimeField(auto_now_add=True, verbose_name='提交订单时间')
    pay_time = models.DateTimeField(auto_now=True, verbose_name='付款时间')
    user = models.ForeignKey(UserProfile, verbose_name='购买的用户')
    total = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='总价格')
    is_pay = models.BooleanField(default=0, verbose_name='是否付款')

    class Meta:
        verbose_name = '订单详情'
        verbose_name_plural = verbose_name
        ordering = ('-id',)

    def __str__(self):
        return str(self.user) + str(self.orderid)


class OrderDetail(models.Model):
    order = models.ForeignKey(OrderMain, verbose_name='订单中心')
    goods_info = models.ForeignKey(GoodsInfo, verbose_name='商品')
    goods_price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='商品价格')
    count = models.IntegerField()

    class Meta:
        verbose_name = '订单详情'
        verbose_name_plural = verbose_name
        ordering = ('-id',)

    def __str__(self):
        return str(self.order) + str(self.goods_info)
