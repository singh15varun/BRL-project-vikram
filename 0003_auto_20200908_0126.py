# Generated by Django 3.1.1 on 2020-09-07 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20200908_0118'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='product',
            name='total_price',
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='subcategory',
            field=models.CharField(default='', max_length=50),
        ),
    ]
