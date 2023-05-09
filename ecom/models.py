from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse

# Create your models here.
class Product(models.Model):
    class ProductClass(models.TextChoices):
        CONSUMABLE = 'con', _('consumable')   
        NON_CONSUMABLE = 'non-con', _('non-consumable')   
    class_name = models.CharField(max_length=300, choices=ProductClass.choices, default=ProductClass.NON_CONSUMABLE)
    sub_class = models.CharField(max_length=300)
    name = models.CharField(max_length=300)
    price = models.DecimalField(max_digits=1000, decimal_places=2)
    description = models.TextField(blank=True)
    image = models.CharField(max_length=300 ,blank=True)
    quantity = models.CharField(max_length=300, blank=True)
    shipping_cost  = models.DecimalField(max_digits=99, null=True, decimal_places=2)



    def get_absolute_url(self):
        return reverse("products:product-detail", kwargs={'id':self.id})

    def __str__(self):
        return self.name