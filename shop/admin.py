from django.contrib import admin
from .models import Product, Order, OrderedProducts, WishlistProduct
# Register your models here.
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderedProducts)
admin.site.register(WishlistProduct)