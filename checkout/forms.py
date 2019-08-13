from django import forms
from .models import Order

class MakePaymentForm(forms.Form):
    MONTH_CHOICES = [(i, i) for i in range(1, 12)]
    YEAR_CHOICES = [(i, i ) for i in range(2019, 2040)]

    credit_debit_card_number = forms.CharField(label='Credit or Debit Card Number', required=False)
    cvv = forms.CharField(label='Security code (CVV)', required=False)
    expiry_month = forms.ChoiceField(label='Month', choices=MONTH_CHOICES, required=False)
    expiry_year = forms.ChoiceField(label='Year', choices=YEAR_CHOICES, required=False)
    stripe_id = forms.CharField(widget=forms.HiddenInput)

class OrderForm(forms.Form):
    class Meta:
        model = Order
        fields = ('customer_firstname', 'customer_lastname', 'customer_phone_number', 'customer_address_line_one', 'customer_address_town', 'customer_address_county', 'customer_country', 'customer_address_post_code', 'date')