from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here to create database.

class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200)

    
    
    # @receiver(post_save, sender=User)
    # def create_customer_profile(sender, instance, created, **kwargs):
    #     if created:
    #         Customer.objects.create(user=instance, name=instance.username, email=instance.email)

    # @receiver(post_save, sender=User)
    # def save_customer_profile(sender, instance, **kwargs):
    #     instance.customer.save()
    

class Product(models.Model):
    # Book details
    a_name = models.CharField(max_length=64)
    b_Language = models.CharField(max_length=64)
    b_title = models.CharField(max_length=64 ,null=True)
    a_about = models.TextField(max_length=500)
    b_description = models.TextField(max_length=800)
    b_genres = models.TextField() 
    b_version = models.IntegerField()
    b_nu_of_pages = models.IntegerField()
    b_price = models.DecimalField(max_digits=99999,decimal_places=2)
    b_rate = models.IntegerField()
    b_y_of_pub = models.DateField()
    b_sound = models.BooleanField(default=False, blank=True)
    b_pic = models.ImageField(null=True, blank=True)
    quantity = models.PositiveIntegerField(default=0)

    # String representation of the book
    



class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100, null=True)

    


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)



class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=200, null=False)
    city = models.CharField(max_length=200, null=False)
    state = models.CharField(max_length=200, null=False)
    zipcode = models.CharField(max_length=200, null=False)
    date_added = models.DateTimeField(auto_now_add=True)


    
class AboutUs(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)


    