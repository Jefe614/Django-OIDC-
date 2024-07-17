from django.contrib import admin
from .models import Customer, Order
# Register your models here.

admin.site.register(Order)
admin.site.register(Customer)