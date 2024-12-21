from django.db import models

# Create your models here.
from django.db import models

# Create your models here to create database.
class BookDetails(models.Model):
    #we need a Year of pub. , we need a author name ,about the author
    #number of book title , version, genres , page_no and description, LANGUAGE.
    a_name = models.CharField(max_length=64)
    b_Language = models.CharField(max_length=64)
    b_title = models.CharField(max_length=64)
    a_about = models.TextField(max_length=500)
    b_review = models.TextField(max_length=400)
    b_description = models.TextField(max_length=800)
    b_genres = models.TextField() 
    b_version = models.IntegerField()
    b_nu_of_pages = models.IntegerField()
    b_price = models.IntegerField()
    b_rate = models.IntegerField()
    b_y_of_pub = models.DateField()
    b_sound = models.BooleanField(default=False)
    b_pic = models.ImageField()

    # this is a string represengtatio of the book 

    def __str__(self):
        return (
            f"ID: {self.id} | Title: {self.b_title} | Genres: {self.b_genres} | "
            f"Description: {self.b_description[:30]}... | Publication Date: {self.b_y_of_pub} | "
            f"Version: {self.b_version} | Pages: {self.b_nu_of_pages} | "
            f"Language: {self.b_Language} | Author: {self.a_name} | "
            f"About Author: {self.a_about[:30]}... | Review: {self.b_review[:30]}... | "
            f"Rating: {self.b_rate}"
        )