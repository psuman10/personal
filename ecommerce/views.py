from django.shortcuts import render, redirect
from django.views import View
from .models import Customer, Product, Cart, OrderPlaced
from .forms import CustomerRegistrationForm, CustomerProfileForm
from django.contrib import messages
from django.db.models import Q
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator



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



class CustomerRegistrationView(View):
    def get(self, request):
        form = CustomerRegistrationForm()
        return render(request, 'BC/customerregistration.html', {'form': form})

    def post(self, request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Congratulations!! Registered Successfully')
            form.save()
        return render(request, 'BC/customerregistration.html', {'form': form, 'active': 'btn-primary'})




def loginVew(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {}
        return render(request, 'BC/login.html', context)


















def address(request):
 return render(request, 'BC/address.html')

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

def add_to_cart(request):
    user = request.user
    product_id = request.GET.get('prod_id')
    product = Product.objects.get(id=product_id)
    Cart(user=user, product=product).save()
    return redirect('/cart')



def show_cart(request):
    totalitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))

        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = 0.0
        shipping_amount = 70.0
        total_amount = 0.0
        cart_product = [p for p in Cart.objects.all() if p.user == user]
        if cart_product:
            for p in cart_product:
                tempamount = (p.quantity * p.product.discounted_price)
                amount += tempamount
                totalamount = amount + shipping_amount
            return render(request, 'BC/addtocart.html', {'carts': cart, 'totalamount': totalamount, 'amount': amount})

        else:
            return render(request, 'BC/emptycart.html')








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
