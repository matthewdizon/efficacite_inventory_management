from django.shortcuts import render, redirect, get_object_or_404
from .models import *

def home(request):
    products = Product.objects.all()
    context = {"products":products}
    return render(request, 'products/index.html', context)