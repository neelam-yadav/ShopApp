from django.conf.urls import url

from .views import NotificationList, OrderDetail, OrderCountView

urlpatterns = [
    url(r'^$', NotificationList.as_view(), name='notifications'),
    url(r'^(?P<pk>\d+)/$', OrderDetail.as_view(), name='order_status'),
]
