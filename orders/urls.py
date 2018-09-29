from django.conf.urls import url

from .views import OrderList, OrderDetail

urlpatterns = [
    url(r'^$', OrderList.as_view(), name='orders'),
    url(r'^(?P<pk>\d+)/$', OrderDetail.as_view(), name='order_detail'),
]
