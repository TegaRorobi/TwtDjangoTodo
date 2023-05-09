from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.views.generic import *

# Create your views here.
class PhoneDetailView(DetailView):
    template_name = 'ecom2/phone_detail.html'
    def get_object(self) :
        id_ = self.kwargs.get('id')
        return get_object_or_404(Phone, id=id_)
