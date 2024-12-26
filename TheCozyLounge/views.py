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
@login_required(login_url='login')
def details_view(request, product_id):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	product = get_object_or_404(Product, id=product_id)# Retrieve the product by ID	
	
	context = {'items':items, 'order':order, 'cartItems':cartItems, 'product': product}
	return render(request, 'store/view.html', context)

