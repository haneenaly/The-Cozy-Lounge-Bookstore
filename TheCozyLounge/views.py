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
