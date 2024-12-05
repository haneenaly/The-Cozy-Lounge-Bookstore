from django.db import models
from django.contrib.auth.models import User



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



