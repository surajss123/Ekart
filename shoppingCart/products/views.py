from django.shortcuts import render
from . models import Products
from django.core.paginator import Paginator
# Create your views here.
def index(request):
    featured_product = Products.objects.order_by('priority')[:4]
    latest_product = Products.objects.order_by('id')[:4]
    context = {
        'featured_product':featured_product,
        'latest_product': latest_product
    }
    return render(request,'index.html',context)
   

def product_list(request):
    page = 1
    if request.GET:
         page = request.GET.get('page',1)
   
    productList = Products.objects.order_by('-priority')
    product_paginator = Paginator(productList,2)
    productList = product_paginator.get_page(page)
    context = {'products':productList}
    return render(request,'products.html',context)

def product_detail(request,pk):
    product = Products.objects.get(pk=pk)
    context = {'product':product}
    return render(request, 'product_details.html',context)

def head(request):
    return render(request, 'header.html')

def product_desc(request):
    return render(request,'product_description.html')
    