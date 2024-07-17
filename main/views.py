from rest_framework import viewsets
from .models import Customer, Order
from django.contrib.auth.decorators import login_required
from .serializers import CustomerSerializer, OrderSerializer
from django.shortcuts import render,redirect
from .forms import OrderForm,CustomerRegistrationForm
from django.contrib import messages



class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

@login_required
def home(request):
    order_form = OrderForm(request.POST or None)
    registration_form = CustomerRegistrationForm(request.POST or None)
    
    if 'registration_success' in request.session:
        registration_success = request.session.pop('registration_success')
        registered_customer = Customer.objects.get(user=request.user)
    else:
        registration_success = False
        registered_customer = None

    if request.method == 'POST':
        if 'order_form_submit' in request.POST:
            if order_form.is_valid():
                order = order_form.save(commit=False)
                order.customer = request.user.customer
                order.save()
                messages.success(request, 'Order submitted successfully!')
                return redirect('home')

        elif 'registration_form_submit' in request.POST:
            if registration_form.is_valid():
                customer = registration_form.save(commit=False)
                customer.user = request.user
                customer.save()
                request.session['registration_success'] = True
                messages.success(request, 'Registration successful!')
                return redirect('home')

    return render(request, 'home.html', {
        'order_form': order_form,
        'registration_form': registration_form,
        'registration_success': registration_success,
        'registered_customer': registered_customer,
    })

def login(request):
    return render(request, 'login.html')

def logout(request):
    return render(request, 'logout.html')
