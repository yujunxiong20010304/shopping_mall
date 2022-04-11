# Generated by Django 3.2 on 2022-04-03 14:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shopping_mall', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False, verbose_name='主键')),
                ('type_one', models.IntegerField(blank=True, db_column='type_one', null=True, verbose_name='类型一')),
                ('type_two', models.IntegerField(blank=True, db_column='type_two', null=True, verbose_name='类型二')),
                ('type_three', models.IntegerField(blank=True, db_column='type_three', null=True, verbose_name='类型三')),
                ('price', models.IntegerField(db_column='price', verbose_name='价格')),
                ('create_date', models.DateTimeField(db_column='last_time', default=django.utils.timezone.now, verbose_name='创建配置的时间')),
                ('modify_date', models.DateTimeField(db_column='creat_time', default=django.utils.timezone.now, verbose_name='修改时间')),
                ('goods_id', models.ForeignKey(db_column='goods_id', on_delete=django.db.models.deletion.CASCADE, to='shopping_mall.goods')),
            ],
            options={
                'db_table': 'price',
            },
        ),
        migrations.CreateModel(
            name='Receiving',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False, verbose_name='主键')),
                ('receiver', models.CharField(db_column='receiver', max_length=5, verbose_name='收货人的姓名')),
                ('phone', models.CharField(db_column='phone', max_length=11, verbose_name='收货人的电话')),
                ('create_date', models.DateTimeField(db_column='creat_time', default=django.utils.timezone.now, verbose_name='创建配置的时间')),
                ('modify_date', models.DateTimeField(db_column='last_time', default=django.utils.timezone.now, verbose_name='修改时间')),
                ('detailed_address', models.CharField(db_column='detailed_address', max_length=225, verbose_name='详细地址')),
                ('city_id', models.OneToOneField(db_column='city_id', on_delete=django.db.models.deletion.CASCADE, to='shopping_mall.city')),
                ('user_id', models.ForeignKey(db_column='user_id', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'receiving',
            },
        ),
        migrations.CreateModel(
            name='ShoppingCart',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False, verbose_name='主键')),
                ('num', models.IntegerField(db_column='num', default=1, verbose_name='购物数量')),
                ('status', models.IntegerField(choices=[(0, '删除'), (1, '购物车'), (2, '待付款'), (3, '待发货'), (4, '取消订单'), (5, '已签收'), (6, '待收货')], db_column='status', default=1, verbose_name='当前购物车商品的存在状态')),
                ('is_assess', models.IntegerField(db_column='is_assess', default=0, verbose_name='是否评价')),
                ('create_date', models.DateTimeField(db_column='creat_time', default=django.utils.timezone.now, verbose_name='创建配置的时间')),
                ('modify_date', models.DateTimeField(db_column='last_time', default=django.utils.timezone.now, verbose_name='修改时间')),
                ('price_id', models.ForeignKey(db_column='price_id', on_delete=django.db.models.deletion.CASCADE, to='user.price')),
                ('receiving', models.OneToOneField(db_column='receive_id', on_delete=django.db.models.deletion.CASCADE, to='user.receiving')),
                ('user_id', models.ForeignKey(db_column='user_id', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'shop_cart',
            },
        ),
        migrations.AddField(
            model_name='price',
            name='members',
            field=models.ManyToManyField(through='user.ShoppingCart', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Assess',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False, verbose_name='主键')),
                ('image', models.ImageField(blank=True, db_column='image', null=True, upload_to='', verbose_name='图片')),
                ('content', models.TextField(db_column='content', verbose_name='文字内容')),
                ('grade', models.IntegerField(db_column='grade', verbose_name='评价等级')),
                ('parents_id', models.IntegerField(blank=True, db_column='parents_id', null=True, verbose_name='父辈的id')),
                ('type', models.IntegerField(db_column='type', default=0, verbose_name='类型')),
                ('create_date', models.DateTimeField(db_column='creat_time', default=django.utils.timezone.now, verbose_name='创建配置的时间')),
                ('modify_date', models.DateTimeField(db_column='last_time', default=django.utils.timezone.now, verbose_name='修改时间')),
                ('state', models.IntegerField(choices=[(0, '删除'), (1, '存在')], db_column='status', default=1)),
                ('goods_id', models.ForeignKey(db_column='goods_id', on_delete=django.db.models.deletion.CASCADE, to='shopping_mall.goods')),
                ('user_id', models.ForeignKey(db_column='user_id', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'assess',
            },
        ),
    ]