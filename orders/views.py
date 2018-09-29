from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.base import View
from django.views.generic import UpdateView, FormView
from django.http import Http404, JsonResponse
from django.shortcuts import redirect

from .mixins import LoginRequiredMixin
from .models import Order
from .forms import OrderStatusForm


# Create your views here.
class OrderStatusUpdate(UpdateView):
    model = Order
    form_class = OrderStatusForm

    def form_valid(self, form):
        form.save()
        return redirect('order_detail')


class OrderCountView(View):
    def get(self, request, *args, **kwargs):
        if request.is_ajax():
            order = Order.objects.all()
            count = order.count()
            return JsonResponse({"count": count})
        else:
            raise Http404


class OrderDetail(FormView, DetailView):
    model = Order
    form_class = OrderStatusForm
    success_url = '/notifications/'

    def get_context_data(self, **kwargs):
        context = super(OrderDetail, self).get_context_data(**kwargs)
        context['form'] = self.get_form()
        return context

    def form_valid(self, form):
        order = Order.objects.get(pk=self.kwargs['pk'])
        form = OrderStatusForm(self.request.POST, instance=order)
        form.save()
        return redirect('notifications')


class OrderList(LoginRequiredMixin, ListView):
    queryset = Order.objects.all()

    def get_queryset(self):
        user_check_id = self.request.user.id
        return super(OrderList, self).get_queryset().filter(user=user_check_id)


class NotificationList(LoginRequiredMixin, ListView):
    queryset = Order.objects.all()
    template_name = "orders/notification_list.html"
