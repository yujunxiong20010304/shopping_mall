import json
from captcha.helpers import captcha_image_url
from captcha.models import CaptchaStore
from django.conf import settings
# 引入发送邮件的模块
from django.core.mail import send_mail
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.views import View
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, SignatureExpired
from oauth.models import User
from django.contrib.auth import authenticate, login


# 创建验证码
def captchas():
    hashkey = CaptchaStore.generate_key()  # 验证码答案
    image_url = captcha_image_url(hashkey)  # 验证码地址
    captcha = {'hashkey': hashkey, 'image_url': image_url}
    return captcha


# 验证验证码是否正确
def jarge_captcha(captchaStr, captchaHashkey):
    if not (captchaStr and captchaHashkey):
        return False
    # 获取根据hashkey获取数据库中的response值
    # get_captcha = get_object_or_404(CaptchaStore, hashkey=captchaHashkey)
    get_captcha = CaptchaStore.objects.filter(hashkey=captchaHashkey)
    if not get_captcha:
        return False
    if get_captcha[0].response == captchaStr.lower():  # 如果验证码匹配
        return True


# 刷新验证码
def refresh_captcha(request):
    return HttpResponse(json.dumps(captchas()), content_type='application/json')


# 登录视图
class LoginView(View):

    @staticmethod
    def get(request):
        hashkey = CaptchaStore.generate_key()  # 验证码答案
        image_url = captcha_image_url(hashkey)  # 验证码地址
        captcha = {'hashkey': hashkey, 'image_url': image_url}
        return render(request, "oauth/login.html", locals())

    @staticmethod
    def post(request):
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        verification = request.POST.get("verification", None)  # 用户提交的验证码
        key = request.POST.get("hashkey", '')  # 验证码答案
        user = authenticate(username=username, password=password)
        if not (jarge_captcha(verification, key) and user):
            return HttpResponse("验证码错误")
        # 登录成功
        login(request, user)    # 保持用户的相关session，这样用户就可以访问登录后才能访问的功能
        return render(request, "shopping/home.html", {})


# 注册视图
class RegisterView(View):
    @staticmethod
    def get(request):
        return render(request, "oauth/register.html", {})

    @staticmethod
    def post(request):
        """ 用户注册验证 """
        # 获取用户注册信息
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        email = request.POST.get('email', None)
        print(username, password)
        # 将用户信息注册进数据库中
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        # 用户邮箱发送激活验证，验证通过就激活，根据唯一标识id来判断是哪个用户
        # 发送的，对用户的id进行加密，防止发生安全隐患
        # 初始化加密器，配置秘钥和超时时间
        serializer = Serializer(settings.SECRET_KEY, 3600)  # 加密方式，加密时间
        info = {'confirm': user.id}  # 获取用户id
        token = serializer.dumps(info)  # 对用户id进行加密
        token = token.decode()  # 默认加密后是byte类型，解密为utf8
        # 发送邮件
        html_message = """<h1>%s,星期天购物欢迎您的到来</h1>请点击以下链接进行激活<br/>
                        <a href="http://127.0.0.1:8000/oauth/active/%s">点击我进行激活</a>""" % (username, token)
        res = send_mail('星期天账号注册', '', '2140585762@qq.com', [email], html_message=html_message)

        # 防止url逆向，
        # return redirect(reverse('goods:index'))
        if res == 1:
            return JsonResponse({'code': 200, 'msg': 'success', 'data': None})
        else:
            return JsonResponse({'code': 404, 'msg': 'fail', 'data': None})


class ActiveView(View):
    @staticmethod
    def get(request, token):
        # 对用户信息进行解密
        serializer = Serializer(settings.SECRET_KEY, 3600)
        try:
            info = serializer.loads(token)
            user_id = info['confirm']  # 获取解密id
            user = User.objects.get(id=user_id)  # 获取用户信息
            user.is_active = 1  # 激活
            user.save()
            # 跳转到登陆页面
            return redirect('/oauth/login')
        except SignatureExpired as e:
            return HttpResponse(status=404, content='对不起，激活时间过期')


# 判断是否已有email和username
def judge_email_username(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        username = User.objects.filter(username=username)
        email = User.objects.filter(email=email)
        if username and email:
            return JsonResponse({'code': 200, 'msg': {'username': 'username', 'email': 'email'}, 'data': None})
        if username:
            return JsonResponse({'code': 200, 'msg': {'username': 'username', 'email': ''}, 'data': None})
        if email:
            return JsonResponse({'code': 200, 'msg': {'username': '', 'email': 'email'}, 'data': None})
        return JsonResponse({'code': 200, 'msg': 'success', 'data': None})
