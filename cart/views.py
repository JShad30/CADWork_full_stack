from django.shortcuts import render, redirect, reverse

"""Create your views here."""
#Render the products within the cart page in the same way as the shop home page
def home(request):
    return render(request, 'cart/home.html')
    


#Function to add the quantities of products
def add_to_cart(request, id):
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})
    if id in cart:
        cart[id] = int(cart[id]) + quantity
    else:
        cart[id] = cart.get(id, quantity)
    request.session['cart'] = cart
    return redirect(reverse('cart-home'))



#Function in the cart to allow the user to be able to change the quantity in the cart.
def adjust_cart(request, id):
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})
    #If statement to check the quantity of products. If they are 0 product to be removed from the cart page.
    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(id)

    request.session['cart'] = cart
    return redirect(reverse('cart-home'))