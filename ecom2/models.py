from django.db import models
from django.urls import reverse

# Create your models here.
class Seller(models.Model):
    name = models.CharField(max_length=1000,blank=False)
    
    location = models.CharField(max_length=1000, blank=False)
    
    contact = models.CharField(max_length=1000, blank=False)

    about = models.TextField(blank=True)
    
    picture_directory = models.CharField(max_length=1000, blank=True, null=True)
    
    type_of_picture = models.CharField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return f'{self.name}, {self.location}, {self.contact}'


class Phone(models.Model):
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE, related_name='phones', null=True)

    name = models.CharField(max_length=1000, blank=False)  #..this is required

    price = models.DecimalField(max_digits=1000, decimal_places=2, blank=False)   #..this is required
    
    quantity = models.IntegerField(blank=False)     #..this is required
    
    brand = models.CharField(max_length=1000, blank=False)  #..this is required
    
    model = models.CharField(max_length=1000, blank=False)  #..this is required
    
    condition = models.CharField(max_length=1000, blank=False)  #..this is required
    
    second_condition = models.CharField(max_length=1000, blank=False)   #..this is required
    
    ram = models.CharField(max_length=1000, blank=False)    #..this is required
    
    internal_storage = models.CharField(max_length=1000, blank=False)   #..this is required
    
    card_slot = models.CharField(max_length=1000, blank=False)   #..this is required
    
    main_camera = models.CharField(max_length=1000, blank=True)
    
    selfie_camera = models.CharField(max_length=1000, blank=True)
    
    operating_system = models.CharField(max_length=1000, blank=True)
    
    color = models.CharField(max_length=1000, blank=False)   #..this is required
    
    battery_life = models.CharField(max_length=1000, blank=False)    #..this is required
    
    screen_size = models.CharField(max_length=1000, blank=False)   #..this is required

    def get_absolute_url(self):
        return reverse('ecom2:phone-detail', kwargs={'id':self.id})

    def __str__(self):
        return f'{self.condition}, {self.name}, {self.price}, {self.seller.name}, {self.seller.location}'

class PhoneImage(models.Model):
    picture_directory = models.CharField(max_length=1000, blank=False)

    type_of_picture = models.CharField(max_length=1000, blank=False)

    original_height = models.IntegerField(blank=True, null=True)

    original_width = models.IntegerField(blank=True, null=True)
    
    phone = models.ForeignKey(Phone, on_delete=models.CASCADE, related_name='image')

    def __str__(self):
        return f'{self.phone.name}'
