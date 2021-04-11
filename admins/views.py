from ecommerce.auth import admin_only
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from ecommerce.models import Product,OrderPlaced,CATEGORY_CHOICES
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, View
from admins.forms import ProductForm
from django.urls import reverse_lazy
from django.http.response import HttpResponseRedirect




@admin_only
@login_required
def get_user(request):
    users_all = User.objects.all()
    users = users_all.filter(is_staff=0)
    context = {
        'users': users,
    }
    return render(request, 'admins/showUser.html', context)
@admin_only
@login_required
def get_admin(request):
    admins_all = User.objects.all()
    admins = admins_all.filter(is_staff=1)
    context = {
        'admins': admins,
    }
    return render(request, 'admins/showAdmin.html', context)

@admin_only
@login_required
def update_user_to_admin(request, user_id):
    user = User.objects.get(id=user_id)
    user.is_staff = True
    user.save()
    messages.add_message(request, messages.SUCCESS, 'User has been updated to Admin')
    return redirect('/admin-dashboard')
    
@admin_only
@login_required
def register_user_admin(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'User Registered Successfully')
            return redirect('/admin-dashboard')
        else:
            messages.add_message(request, messages.ERROR, 'Please provide correct details')
            return render(request, "admins/register-user-admin.html", {'form': form})
    context = {
        'form': UserCreationForm
    }
    return render(request, 'admins/register-user-admin.html', context)


@admin_only
@login_required
def admin_dashboard(request):
    users = User.objects.all()
    user_count = users.filter(is_staff=0).count()
    admin_count = users.filter(is_staff=1).count()
    product_count=Product.objects.all().filter().count()
    order_count=OrderPlaced.objects.all().filter().count()
    context = {
       
        'user_count': user_count,
        'admin_count': admin_count,
        'product_count':product_count,
        'order_count':order_count,
   
    }
    return render(request, 'admins/admin-dashboard.html', context)


@method_decorator(admin_only , name='dispatch')
class AdminProductCreateView(CreateView):
    template_name = "admins/adminproductcreate.html"
    form_class = ProductForm
    success_url = reverse_lazy("adminproductlist")
 
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)



@admin_only
@login_required
def delete_product(request,id):
    if request.method=='POST':
        pi=Product.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/admin-product/list/')
@method_decorator(login_required,name='dispatch')
@method_decorator(admin_only,name='dispatch')



class update_product(View):
    def get(self, request, id):
        pi = Product.objects.get(pk=id)
        fm = ProductForm(instance=pi)
        return render(request, 'admins/productupdate.html', {'form': fm})
        
    def post(self, request, id):
        pi = Product.objects.get(pk=id)
        fm = ProductForm(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
        return HttpResponseRedirect('/admin-product/list/')

@admin_only
@login_required
def delete_order(request,id):
    if request.method=='POST':
        pi=OrderPlaced.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/admin-all-orders')