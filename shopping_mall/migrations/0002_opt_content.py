# Generated by Django 3.2 on 2022-04-05 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping_mall', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='opt',
            name='content',
            field=models.CharField(default='nan', max_length=225),
        ),
    ]
