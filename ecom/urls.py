from django.urls import path
from .views import *

app_name = 'products'
urlpatterns = [
    path('', home),
    path('products/',productlistview.as_view(),name='product-list'),
    path('products/shoes/<int:id>/',productdetailview.as_view(),name='product-detail'),
    path('product-display/', productlistview2.as_view(), name = 'product-display')
]