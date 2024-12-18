#To Handle views and redirects
#render--> Renders an HTML pages with a context dictionary.
#redirect--> Redirects users to another URL.(yro7 page eli ana 3ayzaha)
#get_object_or_404--> get the object it not found error_404
from django.shortcuts import render,redirect
#authenticate-->check the username and password of a user.
#login-->Logs a user into the system and creates a session.
#logout-->Logs a user out and end their session.
from django.contrib.auth import authenticate,login,logout
#import the registrationForm form forms.py
from .forms import CreateUserForm
import json
from django.http import JsonResponse
import datetime
#(ydkhol de emta w de emta ana eli b7dd)
from django.contrib.auth.decorators import login_required
from .models import *
from .utils import cookieCart, cartData, guestOrder
#enable message format to user  
from django.contrib import messages

def registerPage(request):
	#bshofo 3ndo account wla la 
	if request.user.is_authenticated:
		#lw ah yro7 llmain =store bta3na
		return redirect('store')
	else:
		#lw la yalla nt3rf nrof ll registration page bta3tna
		form = CreateUserForm()
		#dost 3la register
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			#n check el m 3lomat valid wla la 3shan n3ml save w nprint el message
			#w nwdeh ll login page 
			if form.is_valid():
				form.save()
				#Fetches the username from the form data.
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + user)
				return redirect('login')
		#btrender el registration page awel 7aga
		context={'form':form}
		return render(request, 'accounts/register.html',context)


def loginPage(request):
	if request.user.is_authenticated:
		return redirect('store')
	else:
		#bro7 ll login page akhod data   
		if request.method == 'POST':
			username = request.POST.get('username')
			password = request.POST.get('password')
			#w 2t2kd s7 wla mn el data eli 3nde 
			user = authenticate(request , username = username, password = password)

			if user is not None:
				#kda el data tmm bro7 b2a llstore
				login(request,user)
				return redirect('store')
			else:
				#fe error btl3 el message de 
				messages.info(request,'Username OR Password is incorrect')
		context={}
		return render(request, 'accounts/login.html',context)    


@login_required(login_url='login')
def logoutUser(request):
	logout(request)
	return redirect('login')


@login_required(login_url='login')
def store(request):
	#get cart data for the user.
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']
	#Retrieves all products from the database 3shan tt3rd fe el home page
	product = Product.objects.all()
	context = {'product':product, 'cartItems':cartItems,'items':items, 'order':order}
	return render(request, 'store/store.html', context)


@login_required(login_url='login')
def checkout(request):
	#lma ados 3la checkout
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

