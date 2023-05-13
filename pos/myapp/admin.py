from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Inventory)
admin.site.register(PaymentOption)
admin.site.register(Store)
admin.site.register(Sale)
admin.site.register(Supplier)