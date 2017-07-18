from django.shortcuts import render, redirect
from django.views.generic import View
from django.db import transaction
from datetime import datetime
from django.utils.decorators import method_decorator

from shop_cart.models import ShopCart
from .models import OrderDetail, OrderMain
from users.models import UserProfile
from utils.my_logger import logger
from users.decorate import check_auth
from utils.use_redis import UseRedis

def save_total_num(buy_num, user_id):
    """把购物车中的购买商品的总量 存放在redis中"""
    total_num = UseRedis.read_from_cache(user_id, "total_num")  # 从redis中取出总数
    if total_num is None:
        total_num = 0
    total_num = total_num + buy_num
    UseRedis.write_to_cache(user_id, "total_num", total_num)  # 写入到redis中


# Create your views here.
class OrderView(View):
    """订单结算视图函数"""

    @method_decorator(check_auth)
    @transaction.atomic
    def post(self, request):
        total_price = 0
        is_commit = True
        total_num = 0  # 用于减去购物中的数量
        cart_id = request.POST.get('cart_id').split('/')
        user_id = request.session.get("user_id")
        user = UserProfile.objects.get(id=user_id)
        cart_obj_list = ShopCart.objects.filter(id__in=cart_id)
        # 设置保存点：
        sid = transaction.savepoint()
        try:
            order_id = datetime.strftime(datetime.now(), '%Y%m%d%H%M%S') + str(user_id)
            # 创建订单中心
            order_info = {'order_id': order_id, 'user': user, 'total': total_price}
            order_main = OrderMain.objects.create(**order_info)
            # 遍历购物车中的信息
            for item in cart_obj_list:
                count = item.count
                goods_ku_cun = item.goods_info.goods_stock
                if count <= goods_ku_cun:  # 购买数量满足库存
                    price = item.goods_info.goods_price
                    total_price = total_price + count * price
                    # 创建订单商品详情
                    goods_order_info = {"order": order_main, 'goods_info': item.goods_info,
                                        'goods_price': price, 'count': item.count}
                    OrderDetail.objects.create(**goods_order_info)
                    # 订单创建完成就修改库存和删除购物车中的数据
                    item.goods_info.goods_stock = goods_ku_cun - count
                    item.goods_info.save()  # 保存变更
                    item.delete()
                    total_num = total_num + count  # 计算应该减去的数量
                else:

                    transaction.savepoint_rollback(sid)  # 库存不足的时候失败 进行回滚
                    is_commit = False
                    # 这路需要进行提示是什么原因
                    break
            # 没有错误就进行提交
            if is_commit:
                order_main.total = total_price
                order_main.save()
                transaction.savepoint_commit(sid)  # 没有问题就进行提交
                # 提交成功后 需要把redis中的购物车的个数减去买过的
                total_num = -total_num  # 买了几个就把购物车中的数量减去几个
                save_total_num(total_num, user_id)
        # 商品订单详情
        except Exception as err:
            logger.error(err)
            is_commit = False
            transaction.savepoint_rollback(sid)  # 出现异常进行回滚
        if is_commit:
            return redirect('/user/user_center_order/')
        else:
            return redirect('/shop_cart/my_cart/')
