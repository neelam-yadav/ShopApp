from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .mixins import LoginRequiredMixin
from .models import Order


# Create your views here.
class OrderDetail(DetailView):
    model = Order


class OrderList(LoginRequiredMixin, ListView):
    queryset = Order.objects.all()

    def get_queryset(self):
        user_check_id = self.request.user.id
        return super(OrderList, self).get_queryset().filter(user=user_check_id)
