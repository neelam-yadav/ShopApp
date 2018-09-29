from django.core.urlresolvers import reverse
from django.db import models
from django.utils.safestring import mark_safe
from django.utils.text import slugify


# Create your models here.
def image_upload_to(instance, filename):
    title = instance.product.title
    slug = slugify(title)
    basename, file_extension = filename.split(".")
    new_filename = "%s-%s.%s" % (slug, instance.id, file_extension)
    return "products/%s/%s" % (slug, new_filename)


class Product(models.Model):
    title = models.CharField(max_length=120)
    image = models.ImageField(upload_to=image_upload_to)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=20)

    class Meta:
        ordering = ["-title"]

    def __unicode__(self):  # def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("product_detail", kwargs={"pk": self.pk})

    def get_image_url(self):
        return self.image.url

    def get_price(self):
        return self.price

    def add_to_cart(self):
        return "%s?item=%s&qty=1" % (reverse("cart"), self.id)

    def remove_from_cart(self):
        return "%s?item=%s&qty=1&delete=True" % (reverse("cart"), self.id)

    def get_title(self):
        return self.title

    def get_html_price(self):
        html_text = "<span class='price'>%s</span>" % self.price
        return mark_safe(html_text)
