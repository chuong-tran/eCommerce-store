# Generated by Django 3.0.8 on 2021-01-19 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_app', '0005_auto_20210119_1517'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='p_image',
            field=models.ImageField(upload_to='items/88/'),
        ),
    ]