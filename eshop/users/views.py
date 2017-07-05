from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.generic import View
from django.contrib.auth.models import make_password
from django.contrib.auth import authenticate, login

from .models import UserProfile
from .forms import RegisterForm, LoginForm


# Create your views here.
def check_username(request):
    """接受ajax请求验证用户名是否是存在的"""
    username = request.GET.get('username')
    count = UserProfile.objects.filter(username=username).count()
    return JsonResponse({"count": count})


class RegisterView(View):
    """用户注册视图类"""

    def get(self, request):
        return render(request, 'user/register.html')

    def post(self, request):
        """用户提交注册数据"""
        user = UserProfile()
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            return self.save_register_info(request, user)
        else:
            # form 验证失败返回form的错误信息
            return render(request, 'user/register.html', locals())

    def save_register_info(self, request, user):
        """保存用户注册的信息"""
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        allow = request.POST.get('allow')
        if password1 != password2 or allow != '1':
            # 判断两次密码输入不同
            err = '两次输入的密码一致'
            err_allow = "请阅读用户使用协议"
            return render(request, 'user/register.html', locals())
        email = request.POST.get('email')
        user.username = username
        user.password = make_password(password1)
        user.email = email
        # 暂时遗留的功能  发送邮箱验证码
        # user.is_active = False
        user.save()
        # TODO 暂时重定向到登陆页面  后面改成重定向到发送邮件成功的页面
        return redirect('/user/login/')


class LoginView(View):
    """登陆视图"""

    def get(self, request):
        username = request.COOKIES.get('username', "")
        return render(request, 'user/login.html', locals())

    def post(self, request):
        print(request.POST)
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                # 调用设置cookie的函数
                return self.check_user(request, user, username)
            else:
                err = "用户名或者密码错误.."
                print(err)
                return render(request, 'user/login.html', locals())
        else:
            # 表单验证错误
            return render(request, 'user/login.html', locals())

    def check_user(self, request, user, username):
        """处理用用户的cookie信息"""
        if user.is_active:
            login(request, user)
            request.session['user_id'] = user.id # 获取用户的id保存在信息中
            response = redirect('/shop/index/')
            # 处理cookie 记录用户名
            if request.POST.get('checkbox') == '1':
                response.set_cookie('username', username)  # 设定cookie
                return response
            elif request.POST.get('checkbox') == None:
                response.delete_cookie('username')  # 删除cookie
                return response
            else:
                return response
        else:
            err = "用户没有激活..请先去激活账户.."
            return render(request, 'user/login.html', locals())


class UserCenterInfoView(View):
    """用户信息中心信息视图类"""

    def get(self, request):
        user_info_list = UserProfile.objects.all()
        return render(request, 'user/user_center_info.html', locals())

class UserCenterOrderView(View):
    """用户信息中心信息视图类"""

    def get(self, request):
        user_info_list = UserProfile.objects.all()
        return render(request, 'user/user_center_order.html', locals())


class UserCenterSiteView(View):
    """用户信息中心信息视图类"""

    def get(self, request):
        user_info_list = UserProfile.objects.all()
        return render(request, 'user/user_center_site.html', locals())

