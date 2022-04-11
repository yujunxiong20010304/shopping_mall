from django.db import models
from oauth.models import User
from django.utils.timezone import now


# 城市表
class City(models.Model):
    id = models.BigAutoField('主键', primary_key=True)
    name = models.CharField('城市名字', max_length=25)
    parent_id = models.IntegerField('父id', null=True, blank=True)
    type = models.IntegerField('级别')


# 商品分类
class Genre(models.Model):
    id = models.BigAutoField(primary_key=True)  # 商品分类的主键
    category = models.CharField('商品类别名', max_length=5)

    class Meta:
        db_table = 'genre'


# 商品总类表
class Goods(models.Model):
    id = models.BigAutoField(primary_key=True)  # 商品的主键
    genre_id = models.ForeignKey(Genre, on_delete=models.CASCADE)
    store = models.CharField('店铺的名称', max_length=125)  # 商品所属店铺
    score = models.IntegerField('商品得分', default=100)  # 由用户评价等级最后得出的分数
    text_introduce = models.TextField('文本介绍')
    title = models.CharField(max_length=225)
    show_image = models.TextField('展示图片')
    image_introduce = models.TextField('图片介绍')  # 将图片地址保存为字符串

    class Meta:
        db_table = 'goods'


# 商品详细选择
class Opt(models.Model):
    CHOICES = (
        (0, '选择颜色'),
        (1, '选择尺码'),
        (2, '选择系列'),
        (3, '选择版本'),
        (4, '选择规格'),
        (5, '选择类别'),
        (6, '选择性别'),
    )
    STATUS = (
        (0, '删除'),
        (1, '存在')
    )
    id = models.BigAutoField(primary_key=True)
    type = models.IntegerField('配置的类型', choices=CHOICES)
    image = models.CharField(max_length=225, null=True)
    content = models.CharField(max_length=225)
    create_date = models.DateTimeField('创建配置的时间', default=now)
    modify_date = models.DateTimeField('修改时间', default=now)
    status = models.IntegerField('存在状态', choices=STATUS, default=1)
    goods_id = models.ForeignKey(Goods, on_delete=models.CASCADE)

    class Meta:
        db_table = 'city'
