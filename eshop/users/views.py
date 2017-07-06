from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.generic import View
from django.contrib.auth.models import make_password
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.db.models import Q

from .models import UserProfile, Receiver, EmailVerifyRecord
from .forms import RegisterForm, LoginForm, ReceiverForm, ModifyForm
from utils.email_send import send_email


# Create your views here.
def check_auth(func):
    """装饰器"""

    def inner(request, *args, **kwargs):
        user_id = request.session.get('user_id')
        if user_id:
            return func(request, *args, **kwargs)
        else:
            return redirect('/user/login/')

    return inner


def check_username(request):
    """接受ajax请求验证用户名是否是存在的"""
    username = request.GET.get('username')
    count = UserProfile.objects.filter(username=username).count()
    return JsonResponse({"count": count})


def user_logout(request):
    """注销函数"""
    logout(request)
    return redirect('/shop/index/')


class CustomBackend(ModelBackend):
    """验证用户可以使用邮箱,电话登陆"""

    def authenticate(self, username=None, password=None, **kwargs):
        print(username)
        print(password)
        try:
            user = UserProfile.objects.get(Q(username=username) | Q(email=username) | Q(telephone_number=username))
            if user.check_password(password):
                return user
        except:
            return None


class RegisterView(View):
    """用户注册视图类"""

    def get(self, request):
        return render(request, 'user/register.html')

    def post(self, request):
        user = UserProfile()
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            return self.save_register_info(request, user)
        else:
            return render(request, 'user/register.html', locals())

    def save_register_info(self, request, user):
        """保存用户注册的信息"""
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        allow = request.POST.get('allow')
        if password1 != password2 or allow != '1':
            err = '两次输入的密码一致'
            err_allow = "请阅读用户使用协议"
            return render(request, 'user/register.html', locals())
        email = request.POST.get('email')
        user.username = username
        user.password = make_password(password1)
        user.email = email
        user.is_active = False
        user.save()
        send_email(email, send_type="注册")
        return redirect('/user/send_success/')


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
                return self.check_user(request, user, username)  # 调用设置cookie的函数
            else:
                err = "用户名或者密码错误.."
                return render(request, 'user/login.html', locals())
        else:
            return render(request, 'user/login.html', locals())

    def check_user(self, request, user, username):
        """处理用用户的cookie信息"""
        if user.is_active:
            login(request, user)
            request.session['user_id'] = user.id  # 获取用户的id保存在信息中
            response = redirect('/shop/index/')
            if request.POST.get('checkbox') == '1':
                response.set_cookie('username', username)  # 设定cookie
            elif request.POST.get('checkbox') == None:
                response.delete_cookie('username')  # 删除cookie
            return response
        else:
            err = "用户没有激活..请先去激活账户.."
            return render(request, 'user/login.html', locals())


class UserCenterInfoView(View):
    """用户信息中心信息视图类"""

    @method_decorator(check_auth)
    def get(self, request):
        url_id = request.GET.get('url_id')
        try:
            user_id = request.session.get('user_id')
            print(user_id)
            user_info_list = UserProfile.objects.get(id=user_id)
        except Exception as err:
            print(err)
        return render(request, 'user/user_center_info.html', locals())


class UserCenterOrderView(View):
    """用户订单信息视图类"""

    @method_decorator(check_auth)
    def get(self, request):
        url_id = request.GET.get('url_id')
        user_id = request.session.get('user_id')
        user_info_list = UserProfile.objects.get(id=user_id)
        return render(request, 'user/user_center_order.html', locals())


class UserCenterSiteView(View):
    """用户信息中心信息视图类"""

    def get_user(self, request):
        """获取用户的信息"""
        user_id = request.session.get('user_id')
        user_info_list = UserProfile.objects.get(id=user_id)  # 获取当前用户的信息
        receiver_info = Receiver.objects.filter(user=user_info_list)  # 返回收货人信息
        return user_info_list, receiver_info

    @method_decorator(check_auth)
    def get(self, request):
        url_id = request.GET.get('url_id')
        print(url_id)
        user_info_list, receiver_info = self.get_user(request)
        return render(request, 'user/user_center_site.html', locals())

    def post(self, request, ):
        user_info_list, receiver_info = self.get_user(request)
        receiver_form = ReceiverForm(request.POST)
        if receiver_form.is_valid():
            self.receiver_save_model(request, user_info_list)
            # TODO 这里该为使用ajax来进行提交 只刷新表单的部分
            return render(request, 'user/user_center_site.html', locals())
        else:
            print(receiver_form.errors)
            return render(request, 'user/user_center_site.html', locals())

    def receiver_save_model(self, request, user_info_list):
        """保存增加收货人的信息"""
        receiver = Receiver()
        receiver.user = user_info_list  # 获取关联的对象  收货人的信息
        receiver.name = request.POST.get('username')
        receiver.city = request.POST.get('city')
        receiver.address = request.POST.get('address')
        receiver.telephone = request.POST.get('telephone')
        receiver.save()


class ModifyAddressView(View):
    """操作收货地址 对地址进行编辑和删除操作"""

    @method_decorator(check_auth)
    def get(self, request):
        # 先去获取当前的用户
        # TODO 把user_id 融合到url中 不在显示在get提交的路径上了
        user = request.session.get('user_id')
        receiver_user_id = request.GET.get("id")
        receiver = Receiver.objects.filter(user=user)
        receiver.filter(id=receiver_user_id).delete()
        # TODO 考虑使用ajax 请求 请求成功后  在前端 进行重定向
        return redirect('/user/user_center_site/')  # 在去请求这个页面 进行页面的刷新 返回


class SendSuccessView(View):
    """发送邮件成功"""

    def get(self, request):
        return render(request, 'user/send_success.html')


class ActiveView(View):
    """邮箱激活"""

    def get(self, request, active_code):
        verify_code = EmailVerifyRecord.objects.filter(code=active_code).first()
        if verify_code is not None:
            email = verify_code.email  # 获取用户的邮箱这样才能知道这个是谁的账户
            user = UserProfile.objects.filter(email=email).first()
            user.is_active = True  # 账户设置为可用
            user.save()
            return redirect('/user/login/')  # 验证成功跳转到登陆页面
        else:
            # 验证失败返回忘记密码页面
            return render(request, 'user/active.html')


class ForgePasswordView(View):
    """忘记密码"""

    def get(self, request):
        return render(request, 'user/forget_password.html')

    def post(self, request):
        email = request.POST.get('email')
        user = UserProfile.objects.filter(email=email).first()
        if user:
            statue = send_email(email, send_type="忘记密码")
            if statue:
                return redirect('/user/send_success/')  # 跳转到邮箱发送成功的页面
            else:
                err = "邮件发送失败 请从新进行申请"
                return render(request, 'user/forget_password.html', locals())
        else:
            err = "邮箱不存在"
            return render(request, 'user/forget_password.html', locals())


class ResetPasswordView(View):
    """重置验证密码"""

    def get(self, request, reset_code):
        verify_code = EmailVerifyRecord.objects.filter(code=reset_code).first()
        if verify_code is not None:
            email = verify_code.email
            # TODO 这里把邮箱进行返回 让前端提交请求的时候把邮箱带过来 这样知道是谁要修改信息的
            return render(request, 'user/reset_password.html', locals())  # 返回重置密码页面
        else:
            return redirect('/user/forget_password')


class ModifyView(View):
    """密码重置"""

    def post(self, request):
        modify_form = ModifyForm(request.POST)
        if modify_form.is_valid():
            password1 = request.POST.get('password1')
            password2 = request.POST.get('password2')
            email = request.POST.get('email')
            if password1 == password2:
                print("拿到的email", email)
                user = UserProfile.objects.get(email=email)
                print("修改密码获取到的", user)
                user.password = make_password(password1)
                user.save()
                return redirect('/user/login/')
            else:
                err = "两次密码输入不一致"
                return render(request, 'user/reset_password.html', locals())  # 返回重置密码页面
        else:
            return render(request, 'user/reset_password.html', locals())  # 返回表单中验证的错误信息
