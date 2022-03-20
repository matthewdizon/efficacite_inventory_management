from django.shortcuts import render, redirect, get_object_or_404
from .models import *

def home(request):
    ingredients = Ingredient.objects.all()
    context = {"ingredients":ingredients}
    return render(request, 'ingredients/index.html', context)

def add_ingredient(request):
    if(request.method=="POST"):
        ingredient_name = request.POST.get('ingredient_name')
        description = request.POST.get('description')
        current_quantity = request.POST.get('current_quantity')
        quantity_threshold = request.POST.get('quantity_threshold')
        metric = request.POST.get('metric')
        created_at = request.POST.get('date')
        # ingredients = request.POST.get('ingredients')
        # print(ingredients)
        
        try:
            # ingredients = Ingredient.objects.filter(pk=ingredients)
            
            instance = Ingredient.objects.create(
                name=ingredient_name,
                description=description,
                current_quantity=current_quantity,
                quantity_threshold=quantity_threshold,
                metric=metric,
                created_at=created_at,
            )
            
            # instance.ingredients.add(ingredients)

            # message="Product created successfully"
            # return redirect(f"/foods?message={message}")
            return redirect(f"/inventory")

        except Exception as e:
            message = e
            # context = {'ingredients':ingredients, 'message':message}
            print(message)
            return render(request, 'ingredients/add_ingredient.html')

    else:
        return render(request, 'ingredients/add_ingredient.html')

def view_ingredient(request, pk):
    ingredient = get_object_or_404(Ingredient, pk=pk)
    if request.GET.get('message') == None:
        context = {"ingredient":ingredient}
    else:
        context = {"ingredient":ingredient, 'message':request.GET.get('message')}
    return render(request, 'ingredients/view_ingredient.html', context)