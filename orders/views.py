from django.shortcuts import render
from cart.cart import Cart
# Create your views here.
from .forms import OrderCreateForm

def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.object.create(
                    order=order,
                    product=item['product'],
                    price=item['product'],
                    quantity=item['quantity']
                )
            cart.clear()
            return render(request, 'created.html', {'order':order})
    else:
        form = OrderCreateForm()
    return render(request, 'created.html', {'cart':cart, 'form':form})
