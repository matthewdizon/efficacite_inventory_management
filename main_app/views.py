from django.shortcuts import render #, redirect, get_object_or_404
# from .models import *

def home(request):
    return render(request, 'main_app/index.html')