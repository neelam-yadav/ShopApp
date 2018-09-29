from django.conf.urls import url

from .views import ProductDetailView, ProductListView, ProductCreate

urlpatterns = [
    url(r'^$', ProductListView.as_view(), name='products'),
    url(r'^create/$', ProductCreate.as_view(), name='product_create'),
    url(r'^(?P<pk>\d+)/$', ProductDetailView.as_view(), name='product_detail'),
]
