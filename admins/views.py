from ecommerce.auth import admin_only
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from ecommerce.models import Product,CATEGORY_CHOICES
from django.utils.decorators import method_decorator
from django.views.generic import CreateView
from admins.forms import ProductForm
from django.urls import reverse_lazy



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
    context = {
       
        'user_count': user_count,
        'admin_count': admin_count,
        'product_count':product_count,
   
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