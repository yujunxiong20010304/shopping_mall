from django.shortcuts import render, HttpResponse


# Create your views here.
# 商店主页
def home(request):
    return render(request, 'shopping/home.html')


# 商店搜索结果展示页
def search(request):
    return render(request, 'shopping/search.html')


# 商品详情页
def shop_details(request):
    return render(request, 'shopping/details_shop.html')
