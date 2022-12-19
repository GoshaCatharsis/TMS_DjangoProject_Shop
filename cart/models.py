from django.db import models
from django.contrib.auth.models import User


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    product = models.ManyToManyField('catalog.Book', blank=True)

    def get_total_price(self):
        return round(sum([book.price for book in self.product.all()]), 2)

    def get_total_quantity(self):
        return len(([book for book in self.product.all()]))

    def display_products(self):
        return ', '.join([book.title for book in self.product.all()])


