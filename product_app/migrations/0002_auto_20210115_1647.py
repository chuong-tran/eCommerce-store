# Generated by Django 3.0.8 on 2021-01-15 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
        migrations.RemoveField(
            model_name='product',
            name='price',
        ),
        migrations.AddField(
            model_name='product',
            name='desc',
            field=models.CharField(default=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=254),
        ),
    ]
