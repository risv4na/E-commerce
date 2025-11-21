from .models import *
from django.forms import ModelForm
from django import forms

class ShippingForm(ModelForm):
    shipping_full_name = forms.CharField(label='', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Full Name'}), required=True)
    shipping_email = forms.CharField(label='', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email'}), required=True)
    shipping_address1 = forms.CharField(label='', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Address 1'}), required=True)
    address_type = forms.CharField(label='', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'like home/office..'}), required=True)
    shipping_city = forms.CharField(label='', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'City'}), required=True)
    shipping_state = forms.CharField(label='', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'State'}), required=True)
    shipping_pincode = forms.CharField(label='', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Pincode'}), required=True)
    shipping_country = forms.CharField(label='', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Country'}), required=True)

    class Meta:
        model = ShippingAddress
        fields = ['shipping_full_name', 'shipping_email', 'shipping_address1', 'address_type', 'shipping_city', 'shipping_state', 'shipping_pincode', 'shipping_country']
    


class PaymentForm(forms.Form):
    card_name = forms.CharField(label='', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Name On Card'}), required=True)
    card_number = forms.CharField(label='', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Card Number'}), required=True)
    card_exp_date = forms.CharField(label='', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Expiration Date'}), required=True)
    card_cvv_number = forms.CharField(label='', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'CVV Number'}), required=True)
    card_number = forms.CharField(label='', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Card Number'}), required=True)
