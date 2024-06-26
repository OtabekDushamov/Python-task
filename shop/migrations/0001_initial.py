# Generated by Django 4.2.11 on 2024-03-31 13:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='shop.category', verbose_name='Родитель')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('amount', models.IntegerField(default=1, verbose_name='Количество')),
                ('price', models.FloatField(default=0, verbose_name='Цена')),
                ('active', models.BooleanField(default=False, verbose_name='Активный')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='shop.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('imageUrl', models.ImageField(upload_to='img/shop', verbose_name='Изоброжения')),
            ],
            options={
                'verbose_name': 'Shop',
                'verbose_name_plural': 'Shops',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Product_image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='img/product', verbose_name='Изоброжение')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='shop.product', verbose_name='Продукт')),
            ],
            options={
                'verbose_name': 'Product image',
                'verbose_name_plural': 'Product images',
                'ordering': ['product'],
            },
        ),
        migrations.AddField(
            model_name='product',
            name='shop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='shop.shop', verbose_name='Магазин'),
        ),
    ]
