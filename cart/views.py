from django.shortcuts import render, redirect, reverse

# Create your views here.
"""Render the products within the cart page in the same way as the shop home page"""
def home(request):
    return render(request, 'cart/home.html')
    
def add_to_cart(request, id):
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})
    if id in cart:
        cart[id] = int(cart[id]) + quantity
    else:
        cart[id] = cart.get(id, quantity)
    request.session['cart'] = cart
    return redirect(reverse('cart-home'))

def adjust_cart(request, id):
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})
    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(id)

    request.session['cart'] = cart
    return redirect(reverse('cart-home'))