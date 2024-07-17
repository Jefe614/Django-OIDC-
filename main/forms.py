from django import forms
from allauth.account.forms import LoginForm
from .models import Order, Customer

class CustomLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer', 'item', 'amount']

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        self.fields['customer'].queryset = Customer.objects.all()

class CustomerRegistrationForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('name', 'code')
        
        