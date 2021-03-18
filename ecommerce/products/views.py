from django.shortcuts import render


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











