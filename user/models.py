from django.db import models
from django.utils.timezone import now

# 收货
from oauth.models import User
from shopping_mall.models import City, Goods


# 用户收货信息表
class Receiving(models.Model):
    id = models.BigAutoField('主键', primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, db_column='user_id')
    receiver = models.CharField('收货人的姓名', max_length=5, db_column='receiver')
    phone = models.CharField('收货人的电话', max_length=11, db_column='phone')
    create_date = models.DateTimeField('创建配置的时间', default=now, db_column='creat_time')
    modify_date = models.DateTimeField('修改时间', default=now, db_column='last_time')
    city_id = models.OneToOneField(City, on_delete=models.CASCADE, db_column='city_id')
    detailed_address = models.CharField('详细地址', max_length=225, db_column='detailed_address')

    class Meta:
        db_table = 'receiving'


# 用户评价
class Assess(models.Model):
    STATE = (
        (0, '删除'),
        (1, '存在')
    )
    id = models.BigAutoField('主键', primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, db_column='user_id')
    goods_id = models.ForeignKey(Goods, on_delete=models.CASCADE, db_column='goods_id')
    image = models.ImageField('图片', null=True, blank=True, db_column='image')
    content = models.TextField('文字内容', db_column='content')
    grade = models.IntegerField('评价等级', db_column='grade')
    parents_id = models.IntegerField('父辈的id', null=True, blank=True, db_column='parents_id')  # 可以为空
    type = models.IntegerField('类型', default=0, db_column='type')
    create_date = models.DateTimeField('创建配置的时间', default=now, db_column='creat_time')
    modify_date = models.DateTimeField('修改时间', default=now, db_column='last_time')
    state = models.IntegerField(choices=STATE, default=1, db_column='status')

    class Meta:
        db_table = 'assess'


# 价格
class Price(models.Model):
    id = models.BigAutoField('主键', primary_key=True)  # 价格的主键
    zero = models.IntegerField(null=True, blank=True, default=None)
    one = models.IntegerField(null=True, blank=True, default=None)
    two = models.IntegerField(null=True, blank=True, default=None)
    three = models.IntegerField(null=True, blank=True, default=None)
    four = models.IntegerField(null=True, blank=True, default=None)
    five = models.IntegerField(null=True, blank=True, default=None)
    six = models.IntegerField(null=True, blank=True, default=None)
    price = models.IntegerField('价格', db_column='price')
    create_date = models.DateTimeField('创建配置的时间', default=now, db_column='last_time')
    modify_date = models.DateTimeField('修改时间', default=now, db_column='creat_time')
    goods_id = models.ForeignKey(Goods, on_delete=models.CASCADE, db_column='goods_id')
    members = models.ManyToManyField(User, through='ShoppingCart')

    class Meta:
        db_table = 'price'


# 购物车表
class ShoppingCart(models.Model):
    STATUS = (
        (0, '删除'),
        (1, '购物车'),   # 购物车
        (2, '待付款'),   # 待付款
        (3, '待发货'),   # 待发货
        (4, '取消订单'),
        (5, '已签收'),
        (6, '待收货'),   # 待收货
    )
    ASSESS = (
        (0, '待评价'),
        (1, '已评价')
    )
    id = models.BigAutoField('主键', primary_key=True)  # 购物车的主键
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, db_column='user_id')
    price_id = models.ForeignKey(Price, on_delete=models.CASCADE, db_column='price_id')
    receiving = models.ForeignKey(Receiving, on_delete=models.CASCADE, db_column='receive_id')
    num = models.IntegerField('购物数量', default=1, db_column='num')
    status = models.IntegerField('当前购物车商品的存在状态', choices=STATUS, default=1, db_column='status')
    is_assess = models.IntegerField('是否评价', default=0, db_column='is_assess', choices=ASSESS)
    create_date = models.DateTimeField('创建配置的时间', default=now, db_column='creat_time')
    modify_date = models.DateTimeField('修改时间', default=now, db_column='last_time')

    class Meta:
        db_table = 'shop_cart'
