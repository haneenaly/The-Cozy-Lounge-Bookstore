#To Handle views and redirects
from django.shortcuts import render,redirect,get_object_or_404
#TO import auth functions from django 
from django.contrib.auth import authenticate,login,logout
#import the registrationForm form forms.py
from .forms import CreateUserForm
from .utils import cookieCart, cartData, guestOrder
from .models import *
import json
import datetime
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.
def registerPage(request):
	if request.user.is_authenticated:
		return redirect('store')
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + user)
				return redirect('login')
			
		context={'form':form}
		return render(request, 'accounts/register.html',context)
 

@login_required(login_url='login')
def logoutUser(request):
	logout(request)
	return redirect('login')

def loginPage(request):
	if request.user.is_authenticated:
		return redirect('store')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password = request.POST.get('password')

			user = authenticate(request , username = username, password = password)

			if user is not None:
				login(request,user)
				return redirect('store')
			else:
				messages.info(request,'Username OR Password is incorrect')
		context={}
		return render(request, 'accounts/login.html',context)   
	

@login_required(login_url='login')
def store(request):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	product = Product.objects.all()
	context = {'product':product, 'cartItems':cartItems,'items':items, 'order':order}
	return render(request, 'store/store.html', context)
@login_required(login_url='login')
def checkout(request):
	print(request)
	data = cartData(request)
	
	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	context = {'items':items, 'order':order, 'cartItems':cartItems}
	return render(request, 'store/checkout.html', context)

def processOrder(request):
	transaction_id = datetime.datetime.now().timestamp()
	data = json.loads(request.body)

	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
	else:
		customer, order = guestOrder(request, data)

	total = float(data['form']['total'])
	order.transaction_id = transaction_id

	#check the total is correct or not 
	if total == float(order.get_cart_total):
		order.complete = True
	order.save()

	if order.shipping == True:
		ShippingAddress.objects.create(
		customer=customer,
		order=order,
		address=data['shipping']['address'],
		city=data['shipping']['city'],
		state=data['shipping']['state'],
		zipcode=data['shipping']['zipcode'],
		)

	return JsonResponse('Payment submitted..', safe=False)

@login_required(login_url='login')
def cart(request):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	context = {'items':items, 'order':order, 'cartItems':cartItems}
	return render(request, 'store/cart.html', context)