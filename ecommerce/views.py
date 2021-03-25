from django.shortcuts import render
from django.views import View
from django.db.models import Q
from .models import  Product,Cart



class ProductView(View):
    def get(self, request):
        totalitem = 0
        wear = Product.objects.filter(category="W")
        BT = Product.objects.filter(category="B")
        Half = Product.objects.filter(category="H")
        ff = Product.objects.filter(category="F")
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
        return render(request, 'BC/home.html', { 'Half': Half,'BT': BT,'ff': ff ,'wear':wear,'totalitem': totalitem})
        


class ProductDetailView(View):
    def get(self, request, pk):
        totalitem = 0
        product = Product.objects.get(pk=pk)
        item_already_in_cart = False
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
            item_already_in_cart = Cart.objects.filter(
                Q(product=product.id) & Q(user=request.user)).exists()
        return render(request, 'BC/productdetail.html', {'product': product,'totalitem': totalitem})
        # return render(request, 'BC/productdetail.html', {'product': product, 'item_already_in_cart': item_already_in_cart, 'totalitem': totalitem})



















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



def Halfface(request, data=None):
    totalitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
    if data == None:
        Half = Product.objects.filter(category='H')
    elif data == 'SteelBird' or data == 'Royal':
        Half = Product.objects.filter(category='H').filter(brand=data)
    elif data == 'Below':
        Half = Product.objects.filter(
            category='H').filter(discounted_price__lt=10000)
    elif data == 'Above':
        Half = Product.objects.filter(
            category='H').filter(discounted_price__gt=10000)
    return render(request, 'BC/HalfFace.html', {'Half': Half, 'totalitem': totalitem})



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

def Wears(request, data=None):
    totalitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
    if data == None:
        wear = Product.objects.filter(category='W')
    elif data == 'Steel Bird' or data == 'Royal':
        wear = Product.objects.filter(category='W').filter(brand=data)
    elif data == 'Below':
        wear = Product.objects.filter(
            category='W').filter(discounted_price__lt=10000)
    elif data == 'Above':
        wear = Product.objects.filter(
            category='W').filter(discounted_price__gt=10000)
    return render(request, 'BC/wears.html', {'wear': wear, 'totalitem': totalitem})




def boot(request, data=None):
    totalitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
    if data == None:
        BT = Product.objects.filter(category='B')
    elif data == 'Steel Bird' or data == 'Royal':
        boots = Product.objects.filter(category='B').filter(brand=data)
    elif data == 'Below':
        BT = Product.objects.filter(
            category='B').filter(discounted_price__lt=10000)
    elif data == 'Above':
        BT = Product.objects.filter(
            category='B').filter(discounted_price__gt=10000)
    return render(request, 'BC/Boot.html', {'BT': BT, 'totalitem': totalitem})
