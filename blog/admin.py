from django.contrib import admin

# Register your models here.
from .models import Author, Entry, Blog
admin.site.register(Author)
admin.site.register(Entry)
admin.site.register(Blog)