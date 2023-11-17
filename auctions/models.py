from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.files import File
from urllib.request import urlopen
from tempfile import NamedTemporaryFile
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _



# DONT FORGET TO MIGRATE AFTER CREATING THIS MODEL
# run to migrate changes to database:
#
# > python manage.py makemigrations
# > python manage.py migrate
#


class User(AbstractUser):
    pass
class Category(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='category_images/', blank=True, null=True)

    def __str__(self):
        return self.name 
    
class AuctionListing(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='listings', default=1)
    title = models.CharField(max_length=64)
    description = models.TextField()
    starting_bid = models.IntegerField()
    image_url = models.CharField(max_length=256, blank=True)
    active = models.BooleanField(default=True)
    category = models.ForeignKey(Category, related_name="listings", on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.title} ({self.starting_bid}) {self.category}"
    
class Bid(models.Model):
    listing = models.ForeignKey(AuctionListing, related_name='bids', on_delete=models.CASCADE)
    amount = models.IntegerField()
    
    def __str__(self):
        return f"{self.amount} on {self.listing}"
    
class Comment(models.Model):
    listing = models.ForeignKey(AuctionListing, related_name='comments', on_delete=models.CASCADE)
    content = models.TextField()
    
    def __str__(self):
        return f"{self.content} on {self.listing}"


