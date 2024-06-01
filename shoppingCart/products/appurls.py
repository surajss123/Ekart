from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('products/', views.product_list),
    path('product_detail/<pk>', views.product_detail, name='product_detail'),
    path('header/', views.head),
    path('product_desc/', views.product_desc)
]