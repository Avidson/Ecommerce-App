from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Item, OrderItem, Order, PostImage  #CheckoutAddress,
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.views import View
from michijapp.form import CheckoutForm
from django.contrib.auth import authenticate, login, logout
from django.views.generic.detail import SingleObjectMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, View
import io
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist
from .form import FormContact, EmailForm
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

#single view of item in our model

from jackhun.models import Items
class SearchResultView(ListView):

    model = Items
    template_name = 'jackhun/jack_search.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Items.objects.filter(
            Q(item_name__icontains=query) | Q(description__icontains=query)
        )
        return object_list

class HomeView(ListView):
    model = Item
    paginate_by = 20
    template_name = "michijapp/mich_homepage.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

#Detail view of each item in our model
class ProductView(DetailView):
    model = Item
    #photos = PostImage.objects.filter(Item)
    template_name = "michijapp/michproduct.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #Add in a QuerySet of all the products
        context['product_list'] = Item.objects.all()
        return context

    def get_object(self):
        obj = super().get_object()
        #Record the last accessed date
        obj.last_viewed = timezone.now()
        obj.save()
        return obj

#profile status
from michijapp.models import Profile

class ProfileView(DetailView):
    model = Profile
    template_name = 'michijapp/profile.html'


#This is code section for add_to_cart
def contact_page(request, *args, **kwargs):
    form = FormContact()
    email = EmailForm()
    profile = Profile.objects.filter()

    if request.method == 'POST':
        form = FormContact(request.POST)
        if form.is_valid():
            success = messages.success(request, 'Message was sent successfully')
            form.save()
    if request.method == 'POST':
        email = EmailForm(request.POST)
        if email.is_valid():
            success = messages.success(request,'Thank you for subscribing')
            email.save()

    context = {'form' : form,
                'email' : email,
                'profile' : profile
    }
    return render(request, "michijapp/mich_contact.html", context)



@login_required
def add_to_cart(request, pk):
    item = get_object_or_404(Item, pk = pk)
    order_item, created = OrderItem.objects.get_or_create(
        item = item,
        user = request.user,
        ordered = False)

    order_qs = Order.objects.filter(user=request.user, ordered=False)

    if order_qs.exists() :
        order = order_qs[0]


        if order.items.filter().exists():
            order_item.quantity +=1
            #time = OrderItems.objects.filter(order_item.start_date)
            order_item.save()
            messages.info(request, "Item has been added")
            return redirect("michijapp:michproduct", pk = pk)

        else:
            order.items.add(order_item)
            messages.info(request, "Item added to your cart")
            return redirect("michijapp:michproduct", pk = pk)
    else:
        start_date = timezone.now()
        order = Order.objects.create(user=request.user, start_date = ordered_date)
        order.items.add(order_item)
        messages.info(request, "Item added to your cart")

@login_required
def remove_from_cart(request, pk):
    item = get_object_or_404(Item, pk = pk)
    order_qs = Order.objects.filter(
        user = request.user,
        ordered = False
    )

    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter().exists():
            order_item = OrderItem.objects.filter(
                item = item,
                user = request.user,
                ordered = False
            )[0]
            order_item.delete()
        messages.info(request, "Item \ ""+order_item.item.item_name+""\ remove from your cart")
        return redirect("michijapp:michproduct", pk = pk)

    else:
        messages.info(request, "This Item not in your cart")
        return redirect("michijapp:michproduct", pk=pk)
    #else:
        #add message doesnt have orders
        #messages.info(request, "You do not have an Order")
        #return redirect("jackhun:jackproduct", pk = pk)


class OrderSummaryView(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        try:

            order = Order.objects.get(user=self.request.user, ordered=False)
            orderitems = OrderItem.objects.order_by()

            def get_total_price(self, **kwargs):
                total = get_total_price()


            context = {
                'object' : order,
                'orderitems' : orderitems,

            }

            return render(self.request, 'michijapp/mich_order_summary.html', context)
        except ObjectDoesNotExist:
            messages.error(self.request, "You do not have an order")
            return redirect("michijapp:home")


#This is code section for reduce_quatity_item
@login_required
def reduce_quantity_item(request, pk):
    item = get_object_or_404(Item, pk = pk)
    order_item = OrderItem.objects.filter(
        item = item,
        user = request.user,
        ordered = False,

        )[0]

    order_qs = Order.objects.filter(user=request.user, ordered=False)

    if order_qs.exists() :
        order = order_qs[0]
        if order.items.filter().exists():
            if order_item.quantity > 1:
                order_item.quantity -= 1
                order_item.save()
                return redirect("michijapp:michproduct", pk=pk)

        else:
            order_item.delete()
            messages.info(request, "Item quatity was updated")
            return redirect("michijapp:cart")
        #else:
        #    messages.info(request, "This Item not in your cart")
        #    return redirect("jackhun:order-summary")
    #else:
    #messages.info(request, "You do not have an Order")
    #return redirect("jackhun:cart")

#search query section


#This is code section for CheckoutView
class CheckoutView(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        form = CheckoutForm()
        context = {
            'form' : form
        }
        return render(self.request, 'michijapp/michcheckout.html', context)

    def post(self, *args, **kwargs):
        form = CheckoutForm(self.request.POST or None)

        try:
            order = Order.object.get(user=self.request.user, ordered=False)
            if form.is_valid():
                street_address = form.cleaned_data.get('street_address')
                apartment_address = form.cleaned_data.get('apartment_address')
                country = form.cleaned_data.get('country')
                zip = form.cleaned_data.get('zip')
                same_billing_address = form.cleaned_data.get('same_billing_address')
                save_info = form.cleaned_data.get('save_info')
                payment_option = form.cleaned_data.get('payment_option')

                checkout_address = CheckoutAddress(
                    user = self.request.user,
                    street_address = street_address,
                    apartment_address = apartment_address,
                    country = country,
                    zip = zip
                )

                checkout_address.save()
                order.checkout_address = checkout_address
                order.save()
                return redirect('michijapp:checkout')
            messages.warning(self.request, "Failed Checkout")
            return redirect('michijapp:checkout')

        except ObjectDoesNotExist:
            messages.error(self.request, "You do not have an order")
            return redirect("michijapp:michproduct")

from jackhun.models import Items, OrderItems, Category
def index_page(request, category_slug=None):

    
    
    model = Category()
    display1 = Item.objects.filter()
    display2 = Items.objects.all()
  
    
    category = None
    categories = Category.objects.all()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        display2 = display2.filter(category=category)
    
   

    paginator = Paginator(display2, 5) #for paginator to display 25 items on each page
    page_number = request.GET.get('page', 1)
    try:
        page_obj = paginator.page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    #cart_count = OrderItems.objects.filter().count()

    context = {
        
        'category' : category,
        'categories' : categories,
        'page_obj' : page_obj,
      

    }
    return render(request, 'index.html', context)
