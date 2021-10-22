from django.shortcuts import render
# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Items, OrderItems, Orders, ProfilePic, EmailSubscription, CheckoutAddress, Category
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.views.generic.detail import SingleObjectMixin
from django.views.generic import ListView, DetailView
import io
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist
from jackhun.form import CheckoutForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .form import FormContact, EmailForm, RegisForm, CheckoutForm
from django.db.models import Q
from .models import Profile
from .cart import Cart
from .forms import CartAddProductForm
from django.views.decorators.http import require_POST
from django.core.paginator import Paginator
# Create your views here..

def HomeView(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    all_items = Items.objects.filter(available=True)
    paginator = Paginator(all_items, 5) #for paginator to display 25 items on each page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        all_items = all_items.filter(category=category)

    #cart_count = OrderItems.objects.filter().count()
    context={
        'category' : category,
        'categories' : categories,
        'all_items': all_items,
        'page_obj' : page_obj,
        
       
    }
    return render(request, "jackhun/jackhomepage.html", context)


class ProductView(DetailView):
    model = Items
    template_name = "jackhun/jackproduct.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context



#@require_POST
#def cart_add(request, product_id):
#    cart = Cart(request)
#    product = get_object_or_404(Items, pk=product_id)
#    form = CartAddProductForm(request.POST)
#    if form.is_valid():
#        cd = form.cleaned_data
#        cart.add(item=item,
#                 quantity=cd['quantity']
#                 )
#    return redirect('jackhun:jackproduct')

#@require_POST
#def cart_remove(request, product_id):
#    cart = Cart(request)
#    product = get_object_or_404(Items, pk=product_id)
#    cart.remove(product)
#    return redirect('jackhun:jackproduct')


#def cart_detail(request):
#    cart = Cart(request)
#    return render(request, 'cart/detail.html', {'cart': cart})


class ProfileView(DetailView):
    model = Profile
    template_name = 'jackhun/profile.html'

def dashboard(request, *args, **kwargs):
    profile = ProfilePic.objects.filter()

    context = {
    'profile' : profile
    }

    return render(request, 'jackhun/dashboard.html', context)

def dashnav(request, *args, **kwargs):

    profile = ProfilePic()
    if request.method == 'POST':
        profile = ProfilePic(requst.POST, request.FILES)
        if profile.is_valid():
            profile.save()
            return HttpResponseRedirect('/success/url/')
    else:
        profile = ProfilePic()


    context ={
        'profile' : profile
    }

    return render(request, 'jackhun/dashnav.html', context)


def contact_page(request, *args, **kwargs):
    form = FormContact()
    email = EmailForm()
    profile = Profile.objects.filter()



    if request.method == 'POST':
        form = FormContact(request.POST)
        if form.is_valid():
            success = messages.success(request, 'Message was sent successfully')


            form.save()
            return redirect('jackhun:home')

    if request.method == 'POST':
        email = EmailForm(request.POST)
        if email.is_valid():
            success = messages.success(request,'Thank you for subscribing')
            email.save()

    #return HttpResponse("<h3> Contact Page</h3>")
    context = {'form' : form,
                'email' : email,
                'profile' : profile

    }
    return render(request, "jackhun/jack_contact.html", context)



@login_required
def add_to_cart(request, pk):
    item = get_object_or_404(Items, pk = pk)
    order_qs = Orders.objects.filter(owner=request.user, ordered=False)
    order_item, created = OrderItems.objects.get_or_create(item = item, owner = request.user, ordered = False, quantity = 1)
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item__pk = item.pk).exists():
            order_item.quantity +=1
            order_item.save()
            messages.info(request, "Check your cart, item has been added")
            return redirect("jackhun:jackproduct", pk = pk)

        else:
            order.items.add(order_item)
            messages.info(request, "Item added to your cart")
            return redirect("jackhun:jackproduct", pk = pk)
    else:
        start_date = timezone.now()
        order = Orders.objects.create(owner=request.user, start_date = start_date)
        order.items.add(order_item)
        messages.info(request, "Item added to your cart")

@login_required
def remove_from_cart(request, pk):
    item = get_object_or_404(Items, pk = pk)
    order_qs = Orders.objects.filter(
        owner = request.user,
        ordered = False
    )

    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter().exists():
            order_item = OrderItems.objects.filter(
                item = item,
                owner = request.user,
                ordered = False
            )[0]
            order_item.delete()
        else:
            return HttpResponse("You don't have this item listed in your cart")
        messages.info(request, "Item remove from your cart")
        return redirect("jackhun:jackproduct", pk = pk)

    else:
        messages.info(request, "This Item not in your cart")
        return redirect("jackhun:jackproduct", pk=pk)
    #else:
        #add message doesnt have orders
        #messages.info(request, "You do not have an Order")
        #return redirect("jackhun:jackproduct", pk = pk)


class OrderSummaryView(LoginRequiredMixin, View):
    #model = Items
    #initial = {'key' : 'value'}
    #template_name = 'jackhun/jack_order_summary'

    def get(self, request, *args, **kwargs):
        try:


            order = Orders.objects.get(owner=self.request.user, ordered=False)
            orderitems = OrderItems.objects.filter(owner=self.request.user)
            checkout = Orders.objects.order_by()
            cart_count = OrderItems.objects.filter(owner=request.user).count()
            image = Items.objects.filter()




            context = {
                'order' : order,
                'orderitems' : orderitems,
                'checkout' : checkout,
                'cart_count' : cart_count,



            }


            return render(self.request, 'jackhun/jack_order_summary.html', context)
        except ObjectDoesNotExist:
            messages.error(self.request, "You do not have an order")
            return redirect("jackhun:home")


#This is code section for reduce_quatity_item
@login_required
def reduce_quantity_item(request, pk):
    item = get_object_or_404(Items, pk = pk)
    order_item = OrderItems.objects.filter(
        item = item,
        owner = request.user,
        ordered = False,

        )[0]

    order_qs = Orders.objects.filter(owner=request.user, ordered=False)

    if order_qs.exists() :
        order = order_qs[0]
        if order.items.filter().exists():
            if order_item.quantity > 1:
                order_item.quantity -= 1
                order_item.save()
                return redirect("jackhun:jackproduct", pk=pk)

        else:
            order_item.delete()
            messages.info(request, "Item quatity was updated")
            return redirect("jackhun:cart")
        #else:
        #    messages.info(request, "This Item not in your cart")
        #    return redirect("jackhun:order-summary")
    #else:
    #messages.info(request, "You do not have an Order")
    #return redirect("jackhun:cart")

from michijapp.models import Item
class SearchResultView(ListView):

    model = Items
    template_name = 'jackhun/jack_search.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Items.objects.filter(
            Q(description__icontains=query)
        )
        return object_list



class CheckoutView(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        form = CheckoutForm()
        order = Orders.objects.get(owner=self.request.user, ordered=False)
        context = {
            'form' : form,
            'order' : order
        }
        return render(self.request, 'jackhun/jackcheckout.html', context)

    def post(self, *args, **kwargs):
        form = CheckoutForm(self.request.POST or None)

        try:
            order = Orders.objects.get(owner=self.request.user, ordered=False)
            amount = order.get_total_price()
            if form.is_valid():
                street_address = form.cleaned_data.get('street_address')
                apartment_address = form.cleaned_data.get('apartment_address')
                tel = form.cleaned_data.get('tel')
                country = form.cleaned_data.get('country')
                zip = form.cleaned_data.get('zip')
                same_billing_address = form.cleaned_data.get('same_billing_address')
                save_info = form.cleaned_data.get('save_info')
                payment_option = form.cleaned_data.get('payment_option')

                checkout_address = CheckoutAddress(
                    owner = self.request.user,
                    street_address = street_address,
                    apartment_address = apartment_address,
                    tel = tel,
                    country = country,
                    zip = zip,
                    payment_option = payment_option
                )

                checkout_address.save()
                order.checkout_address = checkout_address
                order.save()

                if payment_option == 'Paystack':
                    return redirect('jackhun:payment', payment_option='paystack')
                elif payment_option == 'Flutterwave':
                    return redirect('jackhun:payment', payment_option='flutterwave')
                elif payment_option == 'Paymoent On Delivery':
                    return redirect('jackhun:confirmation')
                return redirect('jackhun:confirmation')
            else:
                messages.warning(self.request, "Failed Checkout")
                return redirect('jackhun:checkout')

        except ObjectDoesNotExist:
            messages.error(self.request, "You do not have an order")
            return redirect("jackhun:cart")

def register_page(request, *args, **kwargs):
    form = RegisForm()



    if request.method == "POST":
        form = RegisForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('jackhun:register-done')
        user = form.cleaned_data.get('username')
        #messages.success(request, 'Thank you, account created. Please login')

    else:
        form = RegisForm()

    context = {'form' :form


    }
    return render(request, "register.html", context)





def register_done(request, *args, **kwargs):

    return render(request, 'register_done.html', {})


def navbar_item(request, *args, **kwargs):
    display_item = Items()
    form = FormContact()
    email = EmailForm()
    model = OrderItems()
    cart_count = OrderItems.objects.filter(owner=request.user).count()

    if request.method == 'POST':
       form = FormContact(request.POST)
       if form.is_valid():
           success = messages.success(request, 'Message was sent successfully')
           form.save()


    if request.method == 'POST':
        email = EmailForm(request.POST)
        if email.is_valid():
            email.save()
            notification = messages.success(request, 'Thank you for subscription')

    context = {

    'items' : display_item,
    'form' : form,
    'email' : email,
    'cart_count' : cart_count

   }
    return render(request, "generalnav.html", context)

def about_page(request, *args, **kwargs):

    return render(request, 'jackhun/about.html', {})

def order_confirm(request, *args, **kwargs):
    return render(request, 'jackhun/confirm_order.html', {})

from .models import Payment

class PaymentView(View):
    def get(self, *args, **kwargs):
        order = Orders.objects.get(owner=self.request.user, ordered=False)

        context = {
            'order' : order
        }
        return render(self.request, 'jackhun/payment.html', {})

    def post(self, *args, **kwargs):
        order = Orders.objects.get(owner=self.request.user, ordered=False)
        amount = int(order.get_total_price() * 100) #cents

        return redirect('/')

class CategoryView(View):
    def get(self, *args, **kwargs):
        #query = self.request.GET.get('q')
        display_product = get_object_or_404(Items, category='1')
        #return display_product
        try:
            if display_product == 'Doors':
                return redirect('jackhun:category', category='Doors' )
            elif display_product == 'Television':
                return redirect('jackhun:category', category='Television')




        except ObjectDoesNotExist:
            messages.error(self.request, "No such category")
            return redirect('jackhun:jackproduct')

        context = {
            'category' : display_product,

        }

        return render(self.request, 'jackhun/category.html', {})
