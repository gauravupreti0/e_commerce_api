from django.db import models # type: ignore
from .customer import Customer
from .product import Product

class CartItem(models.Model):
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    added_on = models.DateTimeField(auto_now_add=True)