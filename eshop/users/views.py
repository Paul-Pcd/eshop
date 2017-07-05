from django.shortcuts import render
from django.views.generic import View


class RegisterView(View):
    """用户注册视图类"""
    def get(self, request):
        return render(request, 'user/register.html')

# Create your views here.
class UserCenterInfoView(View):
    """用户信息中心信息视图类"""

    def get(self, request):
        return render(request, 'user/user_center_info.html')
        # return render(request, 'user_base.html')
