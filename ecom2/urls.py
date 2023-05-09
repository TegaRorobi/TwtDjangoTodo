from django.urls import path
from .views import *

app_name = 'ecom2'
urlpatterns = [
    path('<int:id>/', PhoneDetailView.as_view(), name = 'phone-detail')
]