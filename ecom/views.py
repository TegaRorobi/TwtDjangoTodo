from django.shortcuts import render, get_object_or_404
from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    DeleteView,
    UpdateView,
)
from .models import Product

# Create your views here.
def home(request):
    return render(request, 'base.html', {})

class productlistview(ListView):
    template_name =  'product_list.html'
    queryset = Product.objects.all()

class productdetailview(DetailView):
    template_name = 'product_detail.html'
    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Product, id = id_)
        
class productlistview2(ListView):
    template_name = 'productlist2.html'
    queryset = Product.objects.all()