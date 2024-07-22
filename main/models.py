from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='customer')
    name = models.CharField(max_length=100,blank=True, null='')
    code = models.CharField(max_length=10, unique=True, blank=True, null='')

    def __str__(self):
        return self.name
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    item = models.CharField(max_length=100,blank=True, null='')
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    time = models.DateTimeField(auto_now_add=True, db_index=True)


    def __str__(self):
        return f'Order {self.id} for {self.item}'