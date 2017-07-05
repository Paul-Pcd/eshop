from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class UserProfile(AbstractUser):
    """用户信息"""
    gender_type = (
        (0, "女"), (1, "男")
    )
    ni_name = models.CharField(max_length=20, verbose_name='昵称', null=True, blank=True)
    telephone_number = models.IntegerField(max_length=11)
    address = models.CharField(max_length=70)
    gender = models.CharField(max_length=3, choices=gender_type, default=0, verbose_name="性别")
    register_date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name
        ordering = ('id',)

    def __str__(self):
        return self.username


class EmailVerifyRecord(models.Model):
    """邮箱验证"""
    send_type = (
        (0, '注册'), (1, '找回密码')
    )
    code = models.CharField(max_length=20, verbose_name='验证码')
    email = models.EmailField(max_length=30, verbose_name='邮箱')
    send_type = models.CharField(max_length=3, choices=send_type, verbose_name='操作类型')
    send_date = models.DateTimeField(auto_now=True, verbose_name='发送的时间')

    class Meta:
        verbose_name = '邮箱验证'
        verbose_name_plural = verbose_name

    def __str__(self):
        """返回发送的类型"""
        return self.get_send_type_display()
