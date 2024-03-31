from django.db import models
import ast


class Shop(models.Model):

    title = models.CharField("Название", max_length=255)
    description = models.TextField("Описание")
    imageUrl = models.ImageField("Изоброжения", upload_to='img/shop')

    class Meta:
        ordering = ['id',]
        verbose_name = "Shop"
        verbose_name_plural = "Shops"

    def __str__(self) -> str:
        return self.title


class Category(models.Model):

    parent = models.ForeignKey("Category", on_delete=models.RESTRICT, verbose_name="Родитель", null=True, blank=True)
    title = models.CharField("Название", max_length=255)
    description = models.TextField("Описание")

    class Meta:
        ordering = ['id',]
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self) -> str:
        return self.title


class Product(models.Model):

    shop = models.ForeignKey(Shop, on_delete=models.RESTRICT, verbose_name="Магазин")
    category = models.ForeignKey(Category, on_delete=models.RESTRICT, verbose_name="Категория")
    title = models.CharField("Название", max_length=255)
    description = models.TextField("Описание")
    amount = models.IntegerField("Количество", default=1)
    price = models.FloatField("Цена", default=0)
    images = models.CharField("Изоброжения", max_length=99999, null=True, blank=True)
    active = models.BooleanField("Активный", default=False)

    class Meta:
        ordering = ['id',]
        verbose_name = "Product"
        verbose_name_plural = "Products"

    @property
    def get_images(self):
        return ast.literal_eval(self.images)

    def __str__(self) -> str:
        return self.title


class Product_image(models.Model):

    product = models.ForeignKey(Product, on_delete=models.RESTRICT, verbose_name="Продукт")
    image = models.ImageField("Изоброжение", upload_to='img/product')

    class Meta:
        ordering = ['product',]
        verbose_name = "Product image"
        verbose_name_plural = "Product images"

    def __str__(self) -> str:
        return f"{self.product.title} | {self.image.name}"
