from django.contrib import admin

# Register your models here.
from .models import Seller, Phone, PhoneImage
admin.site.register(Seller)
admin.site.register(Phone)
admin.site.register(PhoneImage)