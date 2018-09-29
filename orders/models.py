from decimal import Decimal
from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import pre_save
# Create your models here.
from carts.models import Cart


class UserCheckout(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, null=True, blank=True)
    email = models.EmailField(unique=True)

    def __unicode__(self):
        return self.email


ORDER_STATUS_CHOICES = (
    ('created', 'Created'),
    ('paid', 'Paid'),
    ('shipped', 'Shipped'),
    ('refunded', 'Refunded'),
)


class Order(models.Model):
    status = models.CharField(max_length=120, choices=ORDER_STATUS_CHOICES, default='created')
    cart = models.ForeignKey(Cart)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True)
    order_total = models.DecimalField(max_digits=50, decimal_places=2)
    order_id = models.CharField(max_length=20, null=True, blank=True)

    def __unicode__(self):
        return str(self.cart.id)

    class Meta:
        ordering = ['-id']

    def get_absolute_url(self):
        return reverse("order_detail", kwargs={"pk": self.pk})

    def update_status(self, status, order_id=None):
        self.status = status
        if order_id and not self.order_id:
            self.order_id = order_id
        self.save()


def order_pre_save(sender, instance, *args, **kwargs):
    cart_total = instance.cart.total
    order_total = Decimal(cart_total)
    instance.order_total = order_total


pre_save.connect(order_pre_save, sender=Order)
