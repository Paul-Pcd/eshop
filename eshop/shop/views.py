from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import View
from django.core.paginator import Paginator, InvalidPage, PageNotAnInteger


from .models import GoodsCategory, GoodsInfo, GoodsArea
from utils.my_print import my_print
# 全局的数据库查询使用的是 查询集的惰性 和 缓存
goods_category_list = GoodsCategory.objects.all()
category_list = goods_category_list.values('id', 'category_name')


# Create your views here.
class IndexView(View):
    """index首页视图"""

    def get(self, request):
        goods_list = []
        for item in goods_category_list:
            click_num = item.goodsinfo_set.order_by('-goods_click')[0:4]
            new_list = item.goodsinfo_set.order_by('-id')[0:4]
            goods_list.append({'click_num': click_num, 'new_list': new_list, 'goods_category': item})
        content = {'goods_list': goods_list, 'category_list': category_list}
        return render(request, 'shop/index.html', content)


class DetailView(View):
    """详情页视图"""

    def get(self, request, nid):
        goods_info = GoodsInfo.objects.filter(id=nid).first()
        if request.is_ajax():
            data = goods_info.goods_stock
            return JsonResponse({'data': data})
        content = {'goods_info': goods_info, 'category_list': category_list}
        return render(request, 'shop/detail.html', content)


class ListCheckView(View):
    """list页视图"""

    def get(self, request, nid, current_page="1", ordering="0"):
        # 判断采用那种方式进行数据的检索
        order = '-id'   # 默认的排序的方式
        if ordering == "0" or "":
            order = "-id"
        elif ordering == "1":
            order = '-goods_price'
        elif ordering == "2":
            order = '-goods_click'
        # 检索商品
        current_page = int(current_page)
        goods_category = goods_category_list.filter(id=nid).first()
        goods_info = GoodsInfo.objects.filter(goods_category=goods_category).order_by(order)
        my_print("排序的解雇", order)
        my_print(goods_info)
        # 实现分页
        page = Paginator(goods_info, 2)
        print("hahdfha", page.num_pages)
        current_goods_obj = page.page(current_page)
        page_rang = page.page_range
        # 构建字典返回数据
        content = {'category_list': category_list, 'goods_category': goods_category,
                   'current_goods_obj': current_goods_obj, 'page_rang': page_rang,
                   'current_page': current_page, 'ordering': ordering, 'page': page}
        return render(request, 'shop/list.html', content)


class ListView(View):
    """list页视图"""

    def get(self, request, nid):
        # 判断采用那种方式进行数据的检索
        # 检索商品 默认的是返回当前页面  1 第一页
        current_page = 1
        goods_category = goods_category_list.filter(id=nid).first()
        goods_info = GoodsInfo.objects.filter(goods_category=goods_category).order_by('-id')
        # 实现分页 默认的是5页
        page = Paginator(goods_info, 2)

        current_goods_obj = page.page(current_page)
        page_rang = page.page_range
        # 构建字典返回数据  这里返回的是0 因为0被设置为默认的排序方式
        content = {'category_list': category_list, 'goods_category': goods_category,
                   'current_goods_obj': current_goods_obj, 'page_rang': page_rang,
                   'current_page': current_page, 'ordering': "0", 'page': page}
        return render(request, 'shop/list.html', content)



