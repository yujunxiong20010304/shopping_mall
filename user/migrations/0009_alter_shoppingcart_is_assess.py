# Generated by Django 3.2 on 2022-04-09 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_price_zero'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoppingcart',
            name='is_assess',
            field=models.IntegerField(choices=[(0, '待评价'), (1, '已评价')], db_column='is_assess', default=0, verbose_name='是否评价'),
        ),
    ]
