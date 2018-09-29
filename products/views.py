from django.views.generic import (
    ListView,
    CreateView,
    DetailView
)
from django.shortcuts import redirect

from .models import Product
from .forms import ProductForm


# Create your views here.
class ProductCreate(CreateView):
    model = Product
    form_class = ProductForm

    def form_valid(self, form):
        form.save()
        return redirect('products')


class ProductListView(ListView):
    model = Product
    queryset = Product.objects.all()


class ProductDetailView(DetailView):
    model = Product
