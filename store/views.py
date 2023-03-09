from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from .models import Customer
from .forms import CreateNewCustomer

# Create your views here.

def store(request):
	return render(request, 'store/store.html')

def cart(request):
	return render(request, 'store/cart.html')

def checkout(request):
	return render(request, 'store/checkout.html')

def login(request):
	return render(request, 'store/login.html')

def register(request):
	if request.method == 'POST':
		form = CreateNewCustomer(request.POST)
		if form.is_valid():
			name = form.cleaned_data['name']
			email = form.cleaned_data['email']
			password = form.cleaned_data['password']

			password_hashed = make_password(password)

			customer = Customer(name=name, email=email, password=password_hashed)
			customer.save()

			return redirect('/')
	else:
		form = CreateNewCustomer()

	return render(request, 'store/register.html', {'form':form})