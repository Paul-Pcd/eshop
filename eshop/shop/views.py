from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import View
from django.core.paginator import Paginator, InvalidPage, PageNotAnInteger

from .models import GoodsCategory, GoodsInfo
from utils.use_redis import UseRedis
from utils.my_logger import logger

# from utils.my_print import my_print
# 全局的数据库查询使用的是 查询集的惰性 和 缓存
goods_category_list = GoodsCategory.objects.all()
category_list = goods_category_list.values('id', 'category_name')


# cart_num = ShopCart.objects.

# Create your views here.

class IndexView(View):
    """index首页视图"""

    def get(self, request):
        goods_list = []
        goods_num = 0  # 用户购物车中的商品的数量
        for item in goods_category_list:
            click_num = item.goodsinfo_set.order_by('-goods_click')[0:4]
            new_list = item.goodsinfo_set.order_by('-id')[0:4]
            goods_list.append({'click_num': click_num, 'new_list': new_list, 'goods_category': item})
        user_id = request.session.get('user_id')
        if user_id:
            goods_num = UseRedis.read_from_cache(user_id, "total_num")
            if goods_num is None:
                goods_num = 0
        content = {'goods_list': goods_list, 'category_list': category_list, 'goods_num': goods_num}
        return render(request, 'shop/index.html', content)


class DetailView(View):
    """详情页视图"""

    def get(self, request, nid): # nid  商品的id
        goods_num = 0  # 用户购物车中的商品的数量
        user_id = request.session.get('user_id')  # 获取用户的id 用来区别不同的用户 存入redis'
        goods_info = GoodsInfo.objects.filter(id=nid).first()
        if request.is_ajax():  # 查询商品库存
            data = goods_info.goods_stock
            return JsonResponse({'data': data})
        goods_info.goods_click = goods_info.goods_click + 1  # 商品的点击量加1
        goods_info.save()

        recently_browsed = UseRedis.read_from_cache(user_id, 'recently_browsed')
        if recently_browsed is None:
            recently_browsed = []
        if nid in recently_browsed:
            recently_browsed.remove(nid)
        recently_browsed.append(nid)
        if len(recently_browsed) > 5:
            recently_browsed.pop(0)
        if user_id:
            UseRedis.write_to_cache(user_id, 'recently_browsed', recently_browsed)
        if user_id:
            goods_num = UseRedis.read_from_cache(user_id, "total_num")
            if goods_num is None:
                goods_num = 0
        content = {'goods_info': goods_info, 'category_list': category_list, 'goods_num': goods_num}
        return render(request, 'shop/detail.html', content)


class ListCheckView(View):
    """list页视图"""

    def get(self, request, nid, current_page="1", ordering="0"):
        # 判断采用那种方式进行数据的检索
        goods_num = 0  # 用户购物车中的商品的数量
        oid, order = self.get_order(ordering, request)  # 检索商品
        current_page = int(current_page)
        goods_category = goods_category_list.filter(id=nid).first()
        goods_info = GoodsInfo.objects.filter(goods_category=goods_category).order_by(order)
        # 实现分页
        page = Paginator(goods_info, 2)
        current_goods_obj = page.page(current_page)
        page_rang = page.page_range
        # 获取用户购物车中的数量
        user_id = request.session.get('user_id')
        if user_id:
            goods_num = UseRedis.read_from_cache(user_id, "total_num")
            if goods_num is None:
                goods_num = 0
        # 构建字典返回数据
        content = {'category_list': category_list, 'goods_category': goods_category,
                   'current_goods_obj': current_goods_obj, 'page_rang': page_rang,
                   'current_page': current_page, 'ordering': ordering, 'page': page,
                   "oid": oid, 'goods_num': goods_num}
        response = render(request, 'shop/list.html', content)
        return response

    def get_order(self, ordering, request):
        """排序检索方法"""
        order = '-id'  # 默认的排序的方式
        oid = '1'
        if ordering == "0" or "":
            order = "-id"
        elif ordering == "1":
            # 根据get上来的值来判断采用那种方式进行排序
            oid = request.GET.get('oid')
            if oid == '1':
                order = '-goods_price'
                oid = '2'
            elif oid == '2':
                order = 'goods_price'
                oid = '1'
        elif ordering == "2":
            order = '-goods_click'
        return oid, order


class ListView(View):
    """list页视图"""

    def get(self, request, nid):
        # 判断采用那种方式进行数据的检索
        # 检索商品 默认的是返回当前页面  1 第一页
        goods_num = 0  # 用户购物车中的商品的数量
        current_page = 1
        goods_category = goods_category_list.filter(id=nid).first()
        goods_info = GoodsInfo.objects.filter(goods_category=goods_category).order_by('-id')
        # 实现分页 默认的是5页
        page = Paginator(goods_info, 2)

        current_goods_obj = page.page(current_page)
        page_rang = page.page_range
        # 获取用户购物车中的数量
        user_id = request.session.get('user_id')
        if user_id:
            goods_num = UseRedis.read_from_cache(user_id, "total_num")
            if goods_num is None:
                goods_num = 0
        # 构建字典返回数据  这里返回的是0 因为0被设置为默认的排序方式
        content = {'category_list': category_list, 'goods_category': goods_category,
                   'current_goods_obj': current_goods_obj, 'page_rang': page_rang,
                   'current_page': current_page, 'ordering': "0", 'page': page,
                   'oid': '1', 'goods_num': goods_num}
        return render(request, 'shop/list.html', content)

# class DetailView(View):
#     """采用session实现用户的浏览记录"""
#
#     def get(self, request, nid):
#         goods_info = GoodsInfo.objects.filter(id=nid).first()
#         if request.is_ajax():  # 查询商品库存
#             data = goods_info.goods_stock
#             return JsonResponse({'data': data})
#         goods_info.goods_click = goods_info.goods_click + 1  # 商品的点击量加1
#         goods_info.save()
#         content = {'goods_info': goods_info, 'category_list': category_list}
#         recently_browsed =request.session.get("recently_browsed","").split('/')
#         for item in recently_browsed:
#             if len(item) == 0:
#                 recently_browsed.remove(item)
#         if nid in recently_browsed:
#             recently_browsed.remove(nid)
#         recently_browsed.append(nid)
#         if len(recently_browsed) > 5:
#             recently_browsed.pop(0)
#         recently_browsed = "/".join(recently_browsed)
#         request.session['recently_browsed'] = recently_browsed
#         request.session.set_expiry(None)
#         return render(request, 'shop/detail.html', content)
