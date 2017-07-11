from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import View

from utils.use_redis import UseRedis
from utils.my_logger import logger
from .models import ShopCart


# Create your views here.


class AddCartView(View):
    """添加商品到购物车"""

    def get(self, request, nid):
        user_id = request.session.get('user_id')  # 获取用户的信息 每个用户对应自己自己购买的商品
        if request.is_ajax():
            total_num = request.GET.get('total_num', 0)
            buy_num = request.GET.get('buy_num')
            if buy_num is not None:
                cart = ShopCart.objects.filter(user_id=user_id, goods_info_id=nid).first()
                if cart:
                    cart.count += int(buy_num)
                    cart.save()
                else:
                    ShopCart.objects.create(user_id=user_id, goods_info_id=nid, count=buy_num)
                UseRedis.write_to_cache(user_id, "total_num", total_num)
                content = {'statue': 200}
            else:
                logger.info(total_num)
                content = {'status': 500}
            return JsonResponse(content)


class MyCartView(View):
    """购物车页面"""

    def get(self, request):
        user_id = request.session.get('user_id')
        cart_info = ShopCart.objects.filter(user_id=user_id)
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
