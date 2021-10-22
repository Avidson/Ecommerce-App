from django import forms
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget
from django import forms
from django.db import models
from jackhun.models import Message, EmailSubscription, CheckoutAddress
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

PAYMENT = (
    #('Paystack', 'PayStack'),
    ('Payment Before Delivery', 'Payment Before Delivery'),
    ('Payment On Delivery', 'Payment On Delivery')
)

class CheckoutForm(forms.Form):
    street_address = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'class' : 'form-control',
        'placeholder' : 'Plot 14 Ikolaba'
    }))

    apartment_address = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'class' : 'form-control',
        'placeholder' : 'Apartment of suite'
    }))

    tel = forms.IntegerField(required=True, widget=forms.TextInput(attrs={
        'class' : 'form-control',
        'placeholder' : 'Phone Contact'
    }))


    country = CountryField(blank_label='(select country)').formfield(required=True, widget=CountrySelectWidget(attrs={
        'class' : 'custom-select d-block w-100'
    }))
    zip = forms.CharField(widget=forms.TextInput(attrs={
        'class' : 'form-control',
        'placeholder' : '+234'

    }))

    same_billing_address = forms.BooleanField(required=False)
    save_info = forms.BooleanField(required=False)
    payment_option = forms.ChoiceField(widget=forms.RadioSelect, choices=PAYMENT)

class FormContact(ModelForm):
    class Meta:
        model = Message
        fields = ['full_name', 'phone_contact','email_id', 'your_address', 'leave_a_message']

class EmailForm(ModelForm):
    class Meta:
        model = EmailSubscription
        fields = ['email', 'name']

class RegisForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'email', 'password1', 'password2']
