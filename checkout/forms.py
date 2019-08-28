from django import forms
from .models import Order

"""Creating the forms for the shop checkout"""
#Payment form
class MakePaymentForm(forms.Form):
    MONTH_CHOICES = [(i, i) for i in range(1, 13)]
    YEAR_CHOICES = [(i, i ) for i in range(2019, 2030)]

    credit_card_number = forms.CharField(label='Credit or Debit Card Number', required=True)
    cvv = forms.CharField(label='Security code (CVV)', required=True)
    expiry_month = forms.ChoiceField(label='Expiry Month', choices=MONTH_CHOICES, required=True)
    expiry_year = forms.ChoiceField(label='Expiry Year', choices=YEAR_CHOICES, required=True)
    stripe_id = forms.CharField(widget=forms.HiddenInput)



#Form to take the personal information about the user
class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        #Fields from the models.py file
        fields = ['customer_name', 'customer_address_line_one', 'customer_address_town', 'customer_address_county', 'customer_address_post_code']



"""Payment forms to allow users to pay each other after a job has been completed"""