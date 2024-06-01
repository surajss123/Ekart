from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from . models import Customer
from django.contrib import messages
# Create your views here.
def accounts(request):
    if request.POST and 'register' in request.POST:
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            email = request.POST.get('email')
            address = request.POST.get('address')
            phone = request.POST.get('phone')
            # create user account
            user = User.objects.create_user(username=username,password=password,email=email)

            # create customer account
            customers=Customer.objects.create(user=user,address=address,phone=phone)
            success_message = "User registered Sucessfully"
            messages.success(request, success_message)
        except Exception as e:
            error_message = "Duplicate Username"
            messages.error(request,error_message)

    #Check login
    if request.POST and 'login' in request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user:
            login(request,user)
            return redirect('index')
        else:
            messages.error(request,'invalid user credentials')
    return render(request, 'account.html')

def sign_out(request):
    logout(request)
    return redirect('index')