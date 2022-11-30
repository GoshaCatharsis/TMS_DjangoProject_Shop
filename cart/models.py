from django.db import models


class Cart(models.Model):
    product = models.ForeignKey('catalog.Book', on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField()
    price = models.FloatField()


