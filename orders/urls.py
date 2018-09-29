from django.conf.urls import url

from .views import OrderList, OrderDetail, OrderCountView

urlpatterns = [
    url(r'^$', OrderList.as_view(), name='orders'),
    url(r'^count/$', OrderCountView.as_view(), name='order_count'),
    url(r'^(?P<pk>\d+)/$', OrderDetail.as_view(), name='order_detail'),
]
