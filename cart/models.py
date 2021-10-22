from django.db import models
from django.db import models, migrations
from django.shortcuts import reverse
from django.conf import settings
from PIL import Image
from django.core.files.uploadedfile import SimpleUploadedFile
from djrichtextfield.models import RichTextField
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
from jackhun.models import Items

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=datetime.now)

class CartItem(models.Model):
    product = models.ForeignKey(Items, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.FloatField(blank=True)
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE)

    TAX_AMOUNT = 19.25

    def price_tcc(self):
        return self.price * (1 + TAX_AMOUNT/100.0)

    def __str__(self):
        return self.client + " - " + self.product 
