from django.urls import path
from . import views


app_name = 'shopping'

urlpatterns = [
    path('home/', views.home, name='home'),
]