# Generated by Django 3.2 on 2022-04-06 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping_mall', '0008_goods_show_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='show_image',
            field=models.TextField(verbose_name='展示图片'),
        ),
    ]