# Generated by Django 3.2 on 2022-04-05 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping_mall', '0004_opt_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opt',
            name='image',
            field=models.CharField(max_length=225, null=True),
        ),
    ]
