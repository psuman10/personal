from django.shortcuts import render, redirect
from django.views import View
from .models import Customer, Product, Cart, OrderPlaced,STATUS_CHOICES
from .forms import CustomerRegistrationForm, CustomerProfileForm, LoginForm, ProductForm
from django.contrib import messages
from django.db.models import Q
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, DetailView, TemplateView
from .models import Profile
from .forms import ProfileForm
from django.http.response import HttpResponseRedirect
from .auth import admin_only, unauthenticated_user, user_only
from django.urls import reverse_lazy, reverse





#admins

@method_decorator(admin_only , name='dispatch')
class AdminProductListView(ListView):
    template_name = "admins/adminproductlist.html"
    queryset = Product.objects.all().order_by("-id")
    context_object_name = "allproducts"


@method_decorator(admin_only , name='dispatch')
class AdminProductCreateView(CreateView):
    template_name = "admins/adminproductcreate.html"
    form_class = ProductForm
    success_url = reverse_lazy("adminproductlist")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

@method_decorator(admin_only , name='dispatch')
class AdminOrderDetailView(DetailView):
    template_name = "admins/adminorderdetail.html"
    model = OrderPlaced
    context_object_name = "ord_obj"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["allstatus"] = STATUS_CHOICES
        return context

# @method_decorator(admin_only , name='dispatch')
def AdminOrderListView(request):
    template_name = "admins/adminorderlist.html"
    allorders = OrderPlaced.objects.all().order_by("-id")
    customer=Customer.objects.all().order_by("-id")
    context={'allorders':allorders,"customer":customer}
    return render(request,template_name,context)



@method_decorator(admin_only , name='dispatch') 
class AdminOrderStatuChangeView(View):
    def post(self, request,*args, **kwargs):
        order_id = self.kwargs["pk"]
        print(order_id)
        order_obj = OrderPlaced.objects.get(id=order_id)
        new_status = request.POST.get("status")
        order_obj.status = new_status
        order_obj.save()
        return redirect(reverse_lazy("adminorderdetail", kwargs={"pk": order_id}))















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
        # return render(request, 'BC/productdetail.html', {'product': product,'totalitem': totalitem})
        return render(request, 'BC/productdetail.html', {'product': product, 'item_already_in_cart': item_already_in_cart, 'totalitem': totalitem})



class CustomerRegistrationView(View):
    def get(self, request):
        form = CustomerRegistrationForm()
        return render(request, 'BC/customerregistration.html', {'form': form})

    def post(self, request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Congratulations!! Registered Successfully')
            user=form.save()
            Profile.objects.create(user=user,username=user.username)
        return render(request, 'BC/customerregistration.html', {'form': form, 'active': 'btn-primary'})


@unauthenticated_user
def login_user(request):
    if request.user.is_authenticated:
        return render(request, 'BC/home.html')
    else:
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                user = authenticate(request, username=data['username'],
                                    password=data['password'])
                if user is not None:
                    if not user.is_staff:
                        login(request, user)
                        
                        return redirect('home')
                    elif user.is_staff:
                        login(request, user)
                        return redirect('/admin-dashboard')
                else:
                    messages.add_message(request, messages.ERROR,
                                         'Username or Password is Invalid')
                    return render(request, 'BC/login.html', {'form': form})
    form = LoginForm()
    context = {
        'form': LoginForm
    }
    return render(request, 'BC/login.html', context)



def address(request):
 return render(request, 'BC/address.html')

# def buy_now(request):
#  return render(request, 'BC/buynow.html')

def change_password(request):
 return render(request, 'BC/changepassword.html')

def checkout(request):
    totalitem = 0
    user = request.user
    add = Customer.objects.filter(user=user)
    cart_items = Cart.objects.filter(user=user)
    amount = 0.0
    shipping_amount = 100
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))

    cart_product = [p for p in Cart.objects.all() if p.user == request.user]
    if cart_product:
        for p in cart_product:
            tempamount = (p.quantity * p.product.discounted_price)
            amount += tempamount
        totalamount = amount + shipping_amount
    return render(request, 'BC/checkout.html', {'add': add, 'totalamount': totalamount, 'cart_items': cart_items, 'totalitem': totalitem})

def customerregistration(request):
 return render(request, 'BC/customerregistration.html')

def home(request):
 return render(request, 'BC/home.html')

@login_required
def orders(request):
    totalitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
    op = OrderPlaced.objects.filter(user=request.user)
    return render(request, 'BC/orders.html', {'order_placed': op, 'totalitem': totalitem})

def product_detail(request):
     return render(request, 'BC/productdetail.html')

# def profile(request):
#  return render(request, 'BC/profile.html')

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
        shipping_amount = 100.0
        cart_product = [p for p in Cart.objects.all() if p.user == user]
        if cart_product:
            for p in cart_product:
                tempamount = (p.quantity * p.product.discounted_price)
                amount += tempamount
                totalamount = amount + shipping_amount
            return render(request, 'BC/addtocart.html', {'carts': cart, 'totalamount': totalamount, 'amount': amount,'totalitem':totalitem})

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




class SearchView(TemplateView):
    template_name = "BC/search.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        kw = self.request.GET.get("keyword")
        results = Product.objects.filter(Q(title__icontains=kw))
        context["results"] = results
        return context


def delete_address(request,id):
    if request.method=='POST':
        pi=Customer.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/profile')

class update_address(View):
    def get(self,request,id):
        pi=Customer.objects.get(pk=id)
        fm=CustomerProfileForm(instance=pi)
        return render(request,'BC/Updateaddress.html',{'form':fm})

    def post(self,request,id):
       pi=Customer.objects.get(pk=id)
       fm=CustomerProfileForm(request.POST,instance=pi)
       if fm.is_valid():
         fm.save()
       return HttpResponseRedirect('/profile')


def user_account(request):
    profile = request.user.profile
    form = ProfileForm(instance=profile)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('/profile1')
    context = {'form': form}
    return render(request, 'BC/profile1.html', context)



def plus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity += 1
        c.save()
        amount = 0.0
        shipping_amount = 100.0
        total_amount = 0.0
        cart_product = [p for p in Cart.objects.all() if p.user ==
                        request.user]
        for p in cart_product:
            tempamount = (p.quantity * p.product.discounted_price)
            amount += tempamount

        data = {

            'quantity': c.quantity,
            'amount': amount,
            'totalamount': amount + shipping_amount
        }

        return JsonResponse(data)


def minus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity -= 1
        c.save()
        amount = 0.0
        shipping_amount = 100.0
        total_amount = 0.0
        cart_product = [p for p in Cart.objects.all() if p.user ==
                        request.user]
        for p in cart_product:
            tempamount = (p.quantity * p.product.discounted_price)
            amount += tempamount

        data = {

            'quantity': c.quantity,
            'amount': amount,
            'totalamount': amount + shipping_amount
        }

        return JsonResponse(data)



def remove_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.delete()
        amount = 0.0
        shipping_amount = 100.0
        total_amount = 0.0
        cart_product = [p for p in Cart.objects.all() if p.user ==
                        request.user]
        for p in cart_product:
            tempamount = (p.quantity * p.product.discounted_price)
            amount += tempamount
        data = {
            'amount': amount,
            'totalamount': amount + shipping_amount
        }
        return JsonResponse(data)


def ProfileView(request):
    if request.method=='POST':
        fm= CustomerProfileForm(request.POST)
        if fm.is_valid():
            usr = request.user
            name=fm.cleaned_data['name']
            locality=fm.cleaned_data['locality']
            city=fm.cleaned_data['city']
            state=fm.cleaned_data['state']
            
            
            reg=Customer(user=usr,name=name,locality=locality,city=city,state=state)
    
            reg.save()
            fm= CustomerProfileForm()
            
    else:
        fm= CustomerProfileForm()
    stud=Customer.objects.all()
    print(stud)
    return render(request,'BC/profile.html',{'form':fm,'stu':stud})


@login_required
def payment_done(request):
    totalitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
    user = request.user
    custid = request.GET.get('custid')
    customer = Customer.objects.get(id=custid)
    cart = Cart.objects.filter(user=user)
    for c in cart:
        OrderPlaced(user=user, customer=customer,
                    product=c.product, quantity=c.quantity).save()
        c.delete()
    return redirect("orders")

    return redirect("orders", {'totalitem': totalitem})


