#To Handle views and redirects
from django.shortcuts import render,redirect,get_object_or_404
#TO import auth functions from django 
from django.contrib.auth import authenticate,login,logout
#import the registrationForm form forms.py
from .forms import CreateUserForm
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