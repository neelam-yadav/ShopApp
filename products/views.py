from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

# Create your views here.
from .models import Product


class ProductListView(ListView):
    model = Product
    queryset = Product.objects.all()


class ProductDetailView(DetailView):
    model = Product
