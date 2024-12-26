#To Handle views and redirects
from django.shortcuts import render,redirect
#TO import auth functions from django 
#import the registrationForm form forms.py
from .forms import CreateUserForm
from django.http import JsonResponse
import json
import datetime
from django.contrib.auth.decorators import login_required
from .models import *
from django.contrib import messages

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





