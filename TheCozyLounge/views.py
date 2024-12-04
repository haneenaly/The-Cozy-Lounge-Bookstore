#To Handle views and redirects
from django.shortcuts import render,redirect
#TO import auth functions from django 
from django.contrib.auth import authenticate,login
#import the registrationForm form forms.py
from .models import *
from django.contrib import messages



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

