#To Handle views and redirects
from django.shortcuts import render,redirect,get_object_or_404
#TO import auth functions from django 
from django.contrib.auth import authenticate,login,logout
#import the registrationForm form forms.py
from .forms import CreateUserForm
from django.http import JsonResponse
import json
import datetime
from django.contrib.auth.decorators import login_required
from .models import *
from .utils import cookieCart, cartData, guestOrder
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
def logoutUser(request):
	logout(request)
	return redirect('login')

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
def cart(request):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	context = {'items':items, 'order':order, 'cartItems':cartItems}
	return render(request, 'store/cart.html', context)

@login_required(login_url='login')
def checkout(request):
	print(request)
	data = cartData(request)
	
	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	context = {'items':items, 'order':order, 'cartItems':cartItems}
	return render(request, 'store/checkout.html', context)


@login_required(login_url='login')
def updateItem(request):
	data = json.loads(request.body)
	productId = data['productId']
	action = data['action']
	print('Action:', action)
	print('Product:', productId)

	customer = request.user.customer
	product = Product.objects.get(id=productId)
	order, created = Order.objects.get_or_create(customer=customer, complete=False)

	orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

	if action == 'add':
		orderItem.quantity = (orderItem.quantity + 1)
	elif action == 'remove':
		orderItem.quantity = (orderItem.quantity - 1)

	orderItem.save()

	if orderItem.quantity <= 0:
		orderItem.delete()

	return JsonResponse('Item was added', safe=False)


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
def about_us(request):
	about_content = AboutUs.objects.first() 
	data = cartData(request)
	cartItems = data['cartItems']
	order = data['order']
	items = data['items']
	context = {'items':items, 'order':order, 'cartItems':cartItems,'about_content': about_content }
	return render(request, 'store/about_us.html', context)

@login_required(login_url='login')
def details_view(request, product_id):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	product = get_object_or_404(Product, id=product_id)# Retrieve the product by ID	
	
	context = {'items':items, 'order':order, 'cartItems':cartItems, 'product': product}
	return render(request, 'store/view.html', context)


# Search functionalty (yarab ekrmny wenaby na ghalbana )
@login_required(login_url='login')
def search_view(request):
	data = cartData(request)
	
	query = request.GET.get("q")
	products = Product.objects.filter(b_title__icontains=query).order_by("b_y_of_pub")
	
	cartItems = data['cartItems']
	order = data['order']
	items = data['items']
	
	context ={"products":products,"query":query,'items':items, 'order':order, 'cartItems':cartItems}
	return render(request, 'store/search.html', context)
