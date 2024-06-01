from django.urls import path
from . import views

urlpatterns = [
   path('accounts/', views.accounts),
   path('sign_out/', views.sign_out),
]