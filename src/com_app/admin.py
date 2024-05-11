from django.contrib import admin

# Register your models here.
from .models.product import Product
from .models.sale import Sale
from .models.purchase import Purchase 

admin.site.register(Product)
admin.site.register(Sale)
admin.site.register(Purchase)