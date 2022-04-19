from django.urls import path
from . import views


app_name = 'shopping'

urlpatterns = [
    path('home/', views.HomeView.as_view(), name='home'),
    path('search/', views.SearchView.as_view(), name='search'),
    path('details/', views.DetailsView.as_view(), name='shop_details'),
    path('get_address/', views.get_address, name='address'),
]
