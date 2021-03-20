from django.shortcuts import render
from django.views import View
from .models import  Product


def address(request):
 return render(request, 'BC/address.html')

def add_to_cart(request):
 return render(request, 'BC/addtocart.html')

def buy_now(request):
 return render(request, 'BC/buynow.html')

def change_password(request):
 return render(request, 'BC/changepassword.html')

def checkout(request):
 return render(request, 'BC/checkout.html')

def customerregistration(request):
 return render(request, 'BC/customerregistration.html')

def home(request):
 return render(request, 'BC/home.html')

def login(request):
 return render(request, 'BC/login.html')

def orders(request):
 return render(request, 'BC/orders.html')

def product_detail(request):
 return render(request, 'BC/productdetail.html')

def profile(request):
 return render(request, 'BC/profile.html')



# def Halfface(request, data=None):
#     totalitem = 0
#     if request.user.is_authenticated:
#         totalitem = len(Cart.objects.filter(user=request.user))
#     if data == None:
#         Half = Product.objects.filter(category='H')
#     elif data == 'SteelBird' or data == 'Royal':
#         Half = Product.objects.filter(category='H').filter(brand=data)
#     elif data == 'Below':
#         Half = Product.objects.filter(
#             category='H').filter(discounted_price__lt=10000)
#     elif data == 'Above':
#         Half = Product.objects.filter(
#             category='H').filter(discounted_price__gt=10000)
#     return render(request, 'BC/HalfFace.html', {'Half': Half, 'totalitem': totalitem})



def Fullface(request, data=None):
    totalitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
    if data == None:
        ff = Product.objects.filter(category='F')
    elif data == 'AGV' or data == 'XOR':
        ff = Product.objects.filter(category='F').filter(brand=data)
    elif data == 'Below':
        ff = Product.objects.filter(
            category='F').filter(discounted_price__lt=10000)
    elif data == 'Above':
        ff = Product.objects.filter(
            category='F').filter(discounted_price__gt=10000)
    return render(request, 'BC/FullFace.html', {'ff': ff, 'totalitem': totalitem})