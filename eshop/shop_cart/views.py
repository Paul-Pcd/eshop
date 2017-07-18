from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import View
from django.utils.decorators import method_decorator

from utils.use_redis import UseRedis
from utils.my_logger import logger
from .models import ShopCart
from users.models import UserProfile
from users.decorate import check_auth


# Create your views here.

def save_total_num(buy_num, user_id):
    """把购物车中的购买商品的总量 存放在redis中"""
    total_num = UseRedis.read_from_cache(user_id, "total_num")  # 从redis中取出总数
    if total_num is None:
        total_num = 0
    total_num = total_num + buy_num
    UseRedis.write_to_cache(user_id, "total_num", total_num)  # 写入到redis中


class AddCartView(View):
    """添加商品到购物车"""

    def get(self, request, nid):
        user_id = request.session.get('user_id')  # 获取用户的信息 每个用户对应自己自己购买的商品
        if request.is_ajax():
            buy_num = request.GET.get('buy_num')
            if buy_num is not None:
                save_total_num(int(buy_num), user_id)
                try:
                    cart_obj = ShopCart.objects.filter(user_id=user_id, goods_info_id=nid).first()
                    if cart_obj:
                        cart_obj.count += int(buy_num)
                        cart_obj.save()
                    else:
                        ShopCart.objects.create(user_id=user_id, goods_info_id=nid, count=buy_num)
                    content = {'statue': "1"}
                except Exception as err:
                    logger.error(err)
                    content = {'statue': "0"}
            else:
                content = {'status': "0"}
            return JsonResponse(content)


class UpdateCartview(View):
    """更新数据库中的数量"""

    def get(self, request, nid):
        if request.is_ajax():
            user_id = request.session.get('user_id')  # 获取用户的信息 每个用户对应自己自己购买的商品
            buy_num = request.GET.get('buy_num')  # 获取购买的数量
            if buy_num is not None:
                buy_num = int(buy_num)
                try:
                    cart_obj = ShopCart.objects.filter(goods_info_id=nid).first()
                    before_goods_num = cart_obj.count  # 获取之前数据库中的数量然后计算更改的数量
                    cart_obj.count = buy_num
                    cart_obj.save()
                    change_num = buy_num - before_goods_num  # 计算增加的数量
                    save_total_num(change_num, user_id)
                    content = {'statue': "1"}
                except Exception as err:
                    logger.error(err)
                    content = {'statue': "0"}
            else:
                content = {'statue': "0"}
            return JsonResponse(content)


class DeleteGoodsView(View):
    """删除购物车中的商品"""

    def get(self, request, nid):
        user_id = request.session.get('user_id')
        if request.is_ajax():
            try:
                cart_obj = ShopCart.objects.filter(goods_info_id=nid).first()
                delete_num = (-cart_obj.count)
                cart_obj.delete()
                save_total_num(delete_num, user_id)
                content = {'statue': '1'}
            except Exception as err:
                logger.error(err)
                content = {'statue': '0'}
            return JsonResponse(content)


class OrderView(View):
    """订单页面"""

    @method_decorator(check_auth)
    def get(self, request):
        cart_id = request.session.get('cart_id')
        if cart_id is None:
            cart_id = []
        else:
            cart_id = cart_id.split('/')
        user_id = request.session.get('user_id')
        user = UserProfile.objects.filter(id=user_id).first()
        order_list = ShopCart.objects.filter(id__in=cart_id)
        content = {'order_list': order_list, 'user': user, 'cart_id': cart_id}
        return render(request, 'shop_cart/place_order.html', content)

    @method_decorator(check_auth)
    def post(self, request):
        user_id = request.session.get("user_id")
        user = UserProfile.objects.filter(id=user_id).first()
        cart_id = request.POST.getlist('checkbox')
        order_list = ShopCart.objects.filter(id__in=cart_id)
        cart_id = '/'.join(cart_id)
        content = {'order_list': order_list, 'user': user, 'cart_id': cart_id}
        """
        这里暂时把提交的购物车的放入到session中
        """
        request.session['cart_id'] = cart_id
        return render(request, 'shop_cart/place_order.html', content)


class MyCartView(View):
    """购物车页面"""

    @method_decorator(check_auth)
    def get(self, request):
        user_id = request.session.get('user_id')
        cart_info = ShopCart.objects.filter(user_id=user_id).order_by('-id')
        content = {"cart_info": cart_info}
        return render(request, 'shop_cart/cart.html', content)

        # result = UseRedis.read_from_cache(user_id)
        #           if result is None:  # 构建数据结构为 result = {user_id:{'nid':nid, 'count': count}} 内层为cart的字典
        #               result = {}
        #               cart_info = {}
        #           else:
        #               data = result.get('user_id')
        #               if data.get('nid') == nid:
        #                   data['count'] = data.get('count') + count  # 计算同种商品的数量
        #                   UseRedis.write_to_cache(user_id, result)
        #           cart_info['nid'] = nid
        #           cart_info['count'] = count
        #           result['user_id'] = cart_info
        #           content = {'statue':200}