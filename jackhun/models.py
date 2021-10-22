from django.db import models
# Create your models here.
from django.db import models
from django.db import models, migrations
from django.shortcuts import reverse
from django.conf import settings
from PIL import Image
from django.core.files.uploadedfile import SimpleUploadedFile
from djrichtextfield.models import RichTextField
from django.utils import timezone
import math
from django_countries.fields import CountryField


# Create your models here.
CATEGORY = (
    ('Electronics', 'Electronics'),
    ('Mobile Device', 'Mobile Device'),
    ('Computer Device', 'Computer Device'),
    ('Home Equipment', 'Home Equipment'),
    ('Fashion', 'Fashion'),
    ('Doors', 'Doors'),
    ('Doors Accessories', 'Doors Accessories'),
    ('Television', 'Television'),
    ('Armored Luxury Security Doors','Armored Luxury Security Doors'),
    ('Steel Security Doors', 'Steel Security Doors'),
    ('Toilet Doors', 'Toilet Doors'),
    ('Wall Papers', 'Wall Papers'),
    ('Bycircle', 'Bycircle'),
    ('E Bikes', 'E Bikes'),

)

AVAILABILITY = (
    ('Available', 'Available'),
    ('Sold', 'Sold')
)

LABEL = (
    ('New', 'New'),
    ('Best Seller', 'Best Seller')

)


class Category(models.Model):
    item_name = models.CharField(choices= CATEGORY, max_length=200, db_index=True)
    slug = models.SlugField(max_length=100, unique=True)
    class Meta:
        ordering = ('item_name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'
    def __str__(self):
        return self.item_name
    def get_absolute_url(self):
        return reverse('jackhun:product_list_by_category', args=[self.slug])

class Items(models.Model):
    item_name = models.CharField(max_length=150, db_index=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_price = models.FloatField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    available = models.BooleanField(default=True)
    slug = models.SlugField(max_length=200, db_index=True)
    #label = models.CharField(choices=LABEL, max_length=200, default=False)
    seller_name = models.CharField(max_length=100, default='seller name')
    seller_profile = models.TextField(help_text='Details of your company', default=False)
    seller_address = models.CharField(max_length=300, default='seller address')
    image = models.FileField(upload_to ='images/', default="Upload Image")
    image2 = models.FileField(upload_to='images/', default="Upload Image")
    image3 = models.FileField(upload_to='images/', default="upload Image")
    image4 = models.FileField(upload_to='images/', default="upload Image")
    image5 = models.FileField(upload_to='images/', default="upload Image")
    image6 = models.FileField(upload_to='images/', default="upload Image")

    description = models.TextField(default=False)
    class Meta:
        ordering = ('item_name',)
        index_together = (('id', 'slug'),)
    def __str__(self):
        return self.item_name

    def get_absolute_url(self):
        return reverse("jackhun:jackproduct", kwargs={"pk" : self.pk})

    def get_add_to_cart_url(self):
        return reverse("jackhun:add-to-cart", kwargs={"pk" : self.pk})

    def get_remove_from_cart_url(self):
        return reverse("jackhun:remove-from-cart", kwargs={"pk" : self.pk})

    def get_reduce_quantity_item_url(self):
        return reverse("jackhun:reduce-quantity-item", kwargs={"pk" : self.pk})

class PostImage(models.Model):
    post = models.ForeignKey(Items, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to = 'images')


import datetime
class OrderItems(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(Items, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.quantity} of {self.item.item_name}"
    def get_total_item_price(self):
        return self.quantity * self.item.price
    def get_discount_item_price(self):
        return self.quantity * self.item.discount_price
    def get_amount_saved(self):
        return self.get_total_item_price() - self.get_discount_item_price()

    def get_final_price(self):
        #if self.item.discount_price:
         #   return self.get_discount_item_price()
        return self.get_total_item_price()

class Orders(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItems)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField(default=datetime.datetime.now())
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.owner.username

    def get_total_price(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.get_final_price()
        return total

class Message(models.Model):
    """codes written for my contact page """
    full_name = models.CharField(max_length=50)
    phone_contact = models.IntegerField(null=True, blank=True)
    email_id = models.EmailField(help_text="Enter a valid email address")
    your_address = models.CharField(max_length=100)
    leave_a_message = RichTextField()

    def __str__(self):
        return self.full_name

class EmailSubscription(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.email

class Profile(models.Model):
    #profile_pic = models.ImageField()
    full_name = models.CharField(max_length=200)
    Biography = RichTextField()
    profile_pic = models.FileField(upload_to='images/', default=False)

    def __str__(self):
        return self.full_name
    def get_absolute_url(self):
        return reverse("jackhun:profile", kwargs={"pk" : self.pk})

class ProfilePic(models.Model):
    profile_picture = models.ImageField(upload_to='images/')
    def __str__(self):
        return self.profile_picture

class CheckoutAddress(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    street_address = models.CharField(max_length=100)
    apartment_address = models.CharField(max_length=100)
    tel = models.IntegerField()
    country = CountryField(multiple=False)
    zip = models.CharField(max_length=100)
    payment_option = models.CharField(max_length=100, default='None')


    def __str__(self):
        return self.street_address

class Payment(models.Model):
    paystack_id = models.CharField(max_length=50)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True)
    amount = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.owner.username
