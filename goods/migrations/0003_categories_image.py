# Generated by Django 4.2.7 on 2024-05-25 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0002_alter_products_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='categories',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='goods_images', verbose_name='Изображение'),
        ),
    ]
