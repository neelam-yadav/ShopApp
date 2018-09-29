from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.base import View
from django.http import Http404, JsonResponse

from .mixins import LoginRequiredMixin
from .models import Order


# Create your views here.
class OrderCountView(View):
    def get(self, request, *args, **kwargs):
        if request.is_ajax():
            order = Order.objects.all()
            count = order.count()
            return JsonResponse({"count": count})
        else:
            raise Http404


class OrderDetail(DetailView):
    model = Order


class OrderList(LoginRequiredMixin, ListView):
    queryset = Order.objects.all()

    def get_queryset(self):
        user_check_id = self.request.user.id
        return super(OrderList, self).get_queryset().filter(user=user_check_id)


class NotificationList(LoginRequiredMixin, ListView):
    queryset = Order.objects.all()
    template_name = "orders/notification_list.html"

