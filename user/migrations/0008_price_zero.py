# Generated by Django 3.2 on 2022-04-09 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_auto_20220409_1100'),
    ]

    operations = [
        migrations.AddField(
            model_name='price',
            name='zero',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
    ]
