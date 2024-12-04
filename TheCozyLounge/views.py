#To Handle views and redirects
from django.shortcuts import render,redirect,get_object_or_404
from .forms import CreateUserForm
from django.http import JsonResponse
import json
from .models import *



# Search functionalty (yarab ekrmny wenaby na ghalbana )
def search_view(request):
      query = request.GET.get("q")
      products = Product.objects.filter(b_title__icontains=query).order_by("b_y_of_pub")
      context ={
            "products":products,
            "query":query,
	  }
      return render(request, 'store/search.html', context)
