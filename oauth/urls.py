from django.urls import path, re_path
from . import views

app_name = 'oauth'
urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('login/refresh_captcha/', views.refresh_captcha, name='refresh_captcha'),
    path('register/', views.RegisterView.as_view(), name='register'),
    re_path(r'^active/(?P<token>.*)$', views.ActiveView.as_view(), name='active'),  # 用户激活
    path('judge_email_username/', views.judge_email_username, name='judge')
]
