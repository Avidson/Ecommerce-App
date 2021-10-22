from django.db import models
from django.db import models, migrations
from django.shortcuts import reverse
from django.conf import settings
from PIL import Image
from django.core.files.uploadedfile import SimpleUploadedFile
from djrichtextfield.models import RichTextField


# Create your models here.
CATEGORY = (
    ('Security Door', 'Security Door'),
    ('Window', 'Window'),
    ('Door Accessories', 'Door Accessories')
)

LABEL = (
    ('New', 'New'),
    ('Second Hand', 'Second Hand'),
    ('Best Seller', 'Best Seller')

)

class Item(models.Model):
    item_name = models.CharField(max_length=150)
    price = models.FloatField()
    discount_price = models.FloatField(blank=True, null=True)
    category = models.CharField(
        choices=CATEGORY,
        max_length=20,)
    label = models.CharField(choices=LABEL, max_length=20)
    description = RichTextField()
    image = models.FileField(upload_to='images/', default="Upload Image")
    image2 = models.FileField(upload_to='images/', default="Upload Image")
    image3 = models.FileField(upload_to='images/', default="upload Image")
    image4 = models.FileField(upload_to='images/', default="upload Image")
    image5 = models.FileField(upload_to='images/', default="upload Image")
    image6 = models.FileField(upload_to='images/', default="upload Image")
    #last_viewed = models.DateTimeField()


    def __str__(self):
        return self.item_name

    def get_absolute_url(self):
        return reverse("michijapp:michproduct", kwargs={"pk" : self.pk})

    def get_add_to_cart_url(self):
        return reverse("michijapp:add-to-cart", kwargs={"pk" : self.pk})

    def get_remove_from_cart_url(self):
        return reverse("michijapp:remove-from-cart", kwargs={"pk" : self.pk})

    def get_reduce_quantity_item_url(self):
        return reverse("michijapp:reduce-quantity-item", kwargs={"pk" : self.pk})


class PostImage(models.Model):
    post = models.ForeignKey(Item, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to = 'images/')

    def __str__(self):
        return self.post.item_name

import datetime
class OrderItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    time = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return f"{self.quantity} of {self.item.item_name}"
    def get_total_item_price(self):
        return self.quantity * self.item.price
    def get_discount_item_price(self):
        return self.quantity * self.item.discount_price
    def get_amount_saved(self):
        return self.get_total_item_price() - self.get_discount_item_price()

    def get_final_price(self):
        if self.item.discount_price:
            return self.get_total_item_price()
        return self.get_total_item_price()


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

    def get_total_price(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.get_final_price()
        return total

from django_countries.fields import CountryField

#class CheckoutAddress(models.Model):
   # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
   # street_address = models.CharField(max_length=100)
    #apartment_address = models.CharField(max_length=100)
    #country = CountryField(multiple=False)
   # zip = models.CharField(max_length=100)


   # def __str__(self):
    #    return self.user.username

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
    full_name = models.CharField(max_length=200)
    #profile_pic = models.ImageField()
    Biography = RichTextField()
    profile_pic = models.ImageField(default=False)

    def __str__(self):
        return self.full_name
    def get_absolute_url(self):
        return reverse('michijapp:profile', kwargs={'pk' : self.pk})
