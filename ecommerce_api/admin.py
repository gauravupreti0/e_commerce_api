from django.contrib import admin # type: ignore
from .models.product import Product
from .models.customer import Customer
from .models.cart_item import CartItem
from .models.order import Order

admin.site.register(Product),
admin.site.register(Customer),
admin.site.register(CartItem),
admin.site.register(Order)