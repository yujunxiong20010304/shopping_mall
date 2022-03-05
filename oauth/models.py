from django.db import models
from django.utils.timezone import now


# Create your models here.

class User(models.Model):
    user_id = models.AutoField('用户id', primary_key=True)
    account = models.CharField('账户', max_length=11)
    password = models.CharField('密码', max_length=15)
    mailbox = models.EmailField('邮箱')
    is_active = models.IntegerField('判断是否注册成功', null=True)
    head_portrait = models.CharField('头像', max_length=225, null=True)
    balance = models.IntegerField('余额', default=0)
    created_time = models.DateTimeField('创建时间', default=now)
    last_mod_time = models.DateTimeField('修改时间', default=now)


class ReceivingInformation(models.Model):
    username = models.CharField('收件人姓名', max_length=5)
    telephone_number = models.CharField('电话号码', max_length=11)
    address = models.CharField('收货地址', max_length=225)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_time = models.DateTimeField('创建时间', default=now)
    last_mod_time = models.DateTimeField('修改时间', default=now)
