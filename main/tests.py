from django.test import TestCase
from django.contrib.auth.models import User
from .models import Customer, Order

class CustomerModelTest(TestCase):
    def setUp(self):
        user = User.objects.create_user(username='testuser', password='12345')
        Customer.objects.create(name='Test Customer', code='123', user=user)

    def test_customer_creation(self):
        customer = Customer.objects.get(name='Test Customer')
        self.assertEqual(customer.name, 'Test Customer')
        self.assertEqual(customer.code, '123')

class OrderModelTest(TestCase):
    def setUp(self):
        user = User.objects.create_user(username='testuser', password='12345')
        customer = Customer.objects.create(name='Test Customer', code='123', user=user)
        Order.objects.create(item='Test Order', customer=customer)

    def test_order_creation(self):
        order = Order.objects.get(item='Test Order')
        self.assertEqual(order.item, 'Test Order')
