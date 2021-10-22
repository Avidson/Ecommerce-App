from django import forms
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget
from michijapp.models import EmailSubscription, Message
from django.db import models
from django.forms import ModelForm

PAYMENT = (
    ('S', 'Stripe'),
    ('P', 'Paypal')
)

class CheckoutForm(forms.Form):
    street_address = forms.CharField(widget=forms.TextInput(attrs={
        'class' : 'form-control',
        'placeholder' : 'Plot 14 Broadstreet'
    }))

    apartment_address = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'class' : 'form-control',
        'placeholder' : 'Apartment of suite'
    }))

    country = CountryField(blank_label='(select country)').formfield(widget=CountrySelectWidget(attrs={
        'class' : 'custom-select d-block w-100'
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
