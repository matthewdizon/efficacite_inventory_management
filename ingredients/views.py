from django.shortcuts import render, redirect, get_object_or_404
from .models import *

def home(request):
    ingredients = Ingredient.objects.all()
    context = {"ingredients":ingredients}
    return render(request, 'ingredients/index.html', context)

def view_ingredient(request, pk):
    ingredient = get_object_or_404(Ingredient, pk=pk)
    if request.GET.get('message') == None:
        context = {"ingredient":ingredient}
    else:
        context = {"ingredient":ingredient, 'message':request.GET.get('message')}
    return render(request, 'ingredients/view_ingredient.html', context)