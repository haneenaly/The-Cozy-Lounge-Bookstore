# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from django.contrib.auth.models import User
# from .models import Customer  # Import Customer here
# from .models import Customer, Cart


# @receiver(post_save, sender=User)
# def create_customer(sender, instance, created, **kwargs):
#     if created:
#         Customer.objects.create(
#             user=instance,
#             name=instance.username,
#             email=instance.email
#         )


# @receiver(post_save, sender=Customer)
# def create_cart_for_new_customer(sender, instance, created, **kwargs):
#     if created:
#         Cart.objects.create(customer=instance)  # Create a cart for the new customer
        
        
