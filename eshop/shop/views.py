from django.shortcuts import render
from django.views.generic import View
# Create your views here.
class IndexView(View):
    """index首页视图"""
    def get(self, request):
        return render(request, 'shop/index.html')