from django.urls import path
from . import views


app_name = 'shopping'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('search/', views.search, name='search'),
    path('details/', views.shop_details, name='shop_details'),
]
