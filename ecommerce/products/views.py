from django.shortcuts import render
from . models import Product
from . forms import CustomerProfileForm, ProductForm
from django.views import View





def index(request):
    products = Product.objects.all()

    context = {
        'products': products
    }

    return render(request,'BC/index.html',context)


def ProductView(request):

    form = ProductForm()
    context = {
        'form': form  
    }

    return render(request,'BC/addProduct.html',context)
