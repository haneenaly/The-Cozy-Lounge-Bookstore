from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Product) #this means admin can edit anything in the data base
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
admin.site.register(AboutUs)

