from django.shortcuts import render, redirect
from django.views.generic import View
from .models import GoodsCategory, GoodsInfo, GoodsArea

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
        content = {'goods_info': goods_info, 'category_list': category_list}
        return render(request, 'shop/detail.html', content)


class ListView(View):
    """list页视图"""

    def get(self, request, nid):
        goods_category = goods_category_list.filter(id=nid).first()
        goods_info = GoodsInfo.objects.filter(goods_category=goods_category).order_by('-id')
        content = {'goods_info': goods_info, 'category_list': category_list, 'goods_category': goods_category}
        return render(request, 'shop/list.html', content)
