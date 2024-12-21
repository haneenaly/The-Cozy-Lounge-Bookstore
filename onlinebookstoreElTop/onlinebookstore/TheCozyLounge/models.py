from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here to create database.

class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200)

    def __str__(self):
        return self.name or 'No name'
    
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

    # String representation of the book
    def __str__(self):
        return self.b_title

    @property
    def imageURL(self):
        try:
            url = self.b_pic.url
        except:
            url = ''
        return url



class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.id)

    @property
    def shipping(self):
        shipping = False
        orderitems = self.orderitem_set.all()
        for i in orderitems:
            # if i.product.b_sound == False :  # Assuming `b_sound` indicates a digital product
                shipping = True
        return shipping

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total 

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total 


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.product.b_price * self.quantity  # Use `b_price` for the price field
        return total


class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=200, null=False)
    city = models.CharField(max_length=200, null=False)
    state = models.CharField(max_length=200, null=False)
    zipcode = models.CharField(max_length=200, null=False)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address
    
class AboutUs(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    