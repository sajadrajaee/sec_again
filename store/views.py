from django.shortcuts import render
from .models import *
from .models import Customsers
from django.shortcuts import redirect
from django.contrib.auth import login, logout, authenticate

def signup_view(request):
    if request.method=='post':
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        password = request.POST['password']

        user = Customsers.objects.create(
            name=name,
            phone=phone,
            email=email,
        )
        user.set_password(password)
        
        if user is not None:
            user.save()
            return redirect('store:login')
        
        raise ValueError("something went wrong, plz try again!")
    return render(request, 'store/signup.html')
        

def login_view(request):
    if request.method=='POST':
        name = request.POST['name']
        password = request.POST['password']

        user = authenticate(
            request,
            name=name,
            password=password
        )
        if user is not None:
            login(request, user)
            return redirect('store:home')

def logout_view(request):
    logout(request)
    return render('store:login')

def home(request):
    if request.method=='post':
        product = request.POST['product']
        remove = request.POST['remove']
        cart = request.session['cart']
        if cart:
            quantity = cart['product']
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity -1
                else:
                    cart[product] = quantity +1
            else:
                quantity = 1
        else:
            cart = {}
            cart[product] = 1
        request.session['cart'] = cart
        print('cart', request.session['cart'])
        return redirect('store:home')
    
    return render(request, 'store/home.html',)

def cart(request):
    pass

def checkout_view(request):
    pass

def orders_view(request):
    pass
