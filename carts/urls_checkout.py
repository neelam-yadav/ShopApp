from django.conf.urls import url


from .views import CheckoutView, CheckoutFinalView

urlpatterns = [
    url(r'^$', CheckoutView.as_view(), name='checkout'),
    url(r'^final/$', CheckoutFinalView.as_view(), name='checkout_final'),
]