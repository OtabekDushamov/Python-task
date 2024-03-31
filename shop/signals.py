from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Product_image


@receiver(post_save, sender=Product_image)
def set_product_images(sender, instance: Product_image, **kwargs):
    images = [
        item.image.name
        for item in Product_image.objects.filter(product=instance.product)
    ]
    instance.product.images = f"{images}"
    instance.product.save()
