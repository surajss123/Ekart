from django.shortcuts import render,redirect
from . models import Order,OrderedItem
from products.models import Products
from customers.models import Customer
# Create your views here.

def cart(request):
    user = request.user
    customer = user.customer_profile
    cart_obj,created = Order.objects.get_or_create(
        owner = customer,
        order_status = Order.CART_STAGE
    )
    context = {'cart':cart_obj}
    return render(request, 'cart.html',context)

def add_to_cart(request):
    if request.POST:
        user = request.user
        customer = user.customer_profile
        quantity = int(request.POST.get('quantity'))
        product_id = request.POST.get('product_id')
        print(product_id)
        cart_obj,created = Order.objects.get_or_create(
            owner = customer,
            order_status = Order.CART_STAGE
        )
        product = Products.objects.get(pk=product_id)
        ordered_item,created = OrderedItem.objects.get_or_create(
            product = product,
            owner = cart_obj,
            quantity = quantity
        )
       
        # if created:
        #     ordered_item.quantity = quantity
        #     ordered_item.save()
        # else:
        #     ordered_item.quantity = ordered_item.quantity+quantity
        #     ordered_item.save()
    return redirect('cart')

def remove_item(request,pk):
    item = OrderedItem.objects.get(pk=pk)
    if item:
        item.delete()
    return redirect('cart')

