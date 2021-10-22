from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.views.generic.detail import SingleObjectMixin
from django.views.generic import ListView, DetailView, UpdateView, DetailView
import io
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.decorators.http import require_POST 

from jackhun.models import(
    Items
)
from .cart import Cart
from .forms import CartAddProductForm 

@require_POST 
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Items, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product, quantity=cd['quantity'],
                    override_quantity=cd['override']
                    )
    return redirect('cart:cart_detail')
    

@require_POST
def cart_remove(remove, product_id):
    cart = Cart(request)
    product = get_object_or_404(Items, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')

def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/detail.html', {'cart': cart})

