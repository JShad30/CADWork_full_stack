from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import OrderForm, MakePaymentForm
from django.contrib import messages
from .models import OrderLineItem
from django.conf import settings
from django.utils import timezone
from shop.models import Product
import stripe

stripe.api_key = settings.STRIPE_SECRET

@login_required()
def home(request):
    if request.method == 'POST':
        o_form = OrderForm(request.POST)
        p_form = MakePaymentForm(request.POST)

        if o_form.is_valid() and p_form.is_valid():
            order = o_form.save(commit=False)
            order.date = timezone.now()
            order.save()

            cart = request.session.get('cart', {})
            total = 0
            for id, quantity in cart.items():
                product = get_object_or_404(Product, pk=id)
                total += quantity * product.product_price
                order_line_item = OrderLineItem(
                    order = order,
                    product = product,
                    quantity = quantity
                )
                order_line_item.save()

            try:
                customer = stripe.Charge.create(
                    amount = int(total * 100),
                    currency = 'GBP',
                    description = request.user.email,
                    card = p_form.cleaned_data['stripe_id'],
                )
            except stripe.error.CardError:
                messages.error(request, 'Your card has been declined')

            if customer.paid:
                messages.error(request, 'Your payment has been successfully processed')
                request.session['cart'] = {}
                return redirect(reverse('shop-home'))
            else:
                messages.error(request, 'We were unable to accept your payment')

        else:
            print(p_form.errors)
            messages.error(request, 'We were unable to accept a payment with the credit or debit card you provided.')
    
    else:
        p_form = MakePaymentForm()
        o_form = OrderForm()

    return render(request, 'checkout/home.html', {'o_form': o_form, 'p_form': p_form, 'publishable': settings.STRIPE_PUBLISHABLE})
    




