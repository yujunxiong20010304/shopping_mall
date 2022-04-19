from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.views import View
from user.models import ShoppingCart
from oauth.models import User
from django.db.models import Count, Min, Max, Q
from . import utils
from user.models import Price
from shopping_mall.models import Goods, Opt, City
# Create your views here.
# 商店主页
class HomeView(View):
    @staticmethod
    def get(request):
        min_shops = Goods.objects.all().values('id','score', 'store', 'title', 'show_image').annotate(
            min_price=Min('price__price'))
        min_shops = utils.data_conversion(min_shops)
        # 判断当前用户是否登录
        if request.user.is_authenticated:
            userdata = utils.public_data(request)
            image = request.user.head_portrait
            return render(request, 'shopping/home.html',
                          {'msg': 'success', 'data': {'username': userdata.get('username'),
                                                      'status': userdata.get('status'),
                                                      'image': image,
                                                      'shop': min_shops}
                          })

        return render(request, 'shopping/home.html',{'msg': 'success', 'data':{'shop':min_shops}})
    def post(self, request):
        pass


# 商店搜索结果展示页
class  SearchView(View):
    def get(self, request):
        print(request.GET)
        return render(request, 'shopping/search.html')
    def post(self, request):
        pass


# 商品详情页
class DetailsView(View):
    def get(self, request):
        # 获取到详情网页商品的id
        goods_id = request.GET.get('id', default=None)
        if not goods_id:
            return HttpResponse('查询失败')
        # 根据获取到的商品id去查找对应的商品信息
        goods = Goods.objects.filter(id=goods_id).values()                      # 商品信息
        opt = Opt.objects.filter(goods_id_id=goods_id).values('id','type','content','image').order_by('-type')
        opt = utils.shop_category(opt)                   # 商品配置
        price_section = Price.objects.filter(goods_id=goods_id).all().aggregate(Min('price'),Max('price'))
        # 详情商品图片的显示
        images = eval(goods[0].get('show_image'))
        userdata = utils.public_data(request)
        # 计算该商品的累计评价数
        evaluate_num = Price.objects.filter(goods_id=goods_id).values('shoppingcart__id','shoppingcart__is_assess')\
            .exclude(shoppingcart__id=None).filter(shoppingcart__is_assess=0).distinct().count()
        """:展示使用"""
        min_shops = Goods.objects.all().values('id', 'score', 'store', 'title', 'show_image').annotate(
            min_price=Min('price__price'))
        min_shops = utils.data_conversion(min_shops)

        return render(request, 'shopping/details_shop.html', {'msg': 'success','data':{
            'goods': goods,
            'opt': opt,
            'price': price_section,
            'images': images,
            'username': userdata.get('username'),
            'status': userdata.get('status'),
            'evaluate_num': evaluate_num,
            "min_shops": min_shops,
        }})

    def post(self, request):
        result = request.POST.get('result', default=None)
        result = eval(result)
        if result:
            price = Price.objects.filter(
                Q(zero=result.get('zero')),
                Q(one=result.get('one')),
                Q(two=result.get('two')),
                Q(three=result.get('three')),
                Q(four=result.get('four')),
                Q(five=result.get('five')),
                Q(six=result.get('six'))).all().values('price')
            if not price:
                return JsonResponse({'code': 200, 'msg': 'no data', 'data': None})
            return JsonResponse({'code': 200, 'msg': 'success', 'data': price[0]})
        return JsonResponse({'code': 200, 'msg': 'fail', 'data': None})

def get_address(request):
    address_id = request.POST.get('id', default=None)
    type = request.POST.get('type', default=None)
    if (address_id and type):
        address = City.objects.filter(parent_id=address_id).values()
        if not address:
            return JsonResponse({'code': 200, 'msg': 'fail', 'data': {}})
    else:
        test = City.objects.filter(id=address_id).values('parent_id')
        address = City.objects.filter(parent_id=test[0]['parent_id']).values()
        print(address)
    return JsonResponse({'code': 200, 'msg': 'success', 'data': {'address':list(address)}})
