from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from suppliers.models import Supplier

def home(request):
    ingredients = Ingredient.objects.all()
    print(ingredients[0].current_quantity/ingredients[0].quantity_threshold)
    context = {"ingredients":ingredients}
    return render(request, 'ingredients/index.html', context)

def add_ingredient(request):
    supplier_objects = Supplier.objects.all()
    context = {'suppliers':supplier_objects}

    if(request.method=="POST"):
        ingredient_name = request.POST.get('ingredient_name')
        description = request.POST.get('description')
        current_quantity = request.POST.get('current_quantity')
        quantity_threshold = request.POST.get('quantity_threshold')
        metric = request.POST.get('metric')
        created_at = request.POST.get('date')
        supplier_id = request.POST.get('supplier')

        print(supplier_id)

        supplier = Supplier.objects.filter(pk=supplier_id)
        print(supplier)
        
        # suppliers = Ingredient.objects.filter(pk__in=supplier_ids)
        # print(suppliers)
        
        try:
            instance = Ingredient.objects.create(
                name=ingredient_name,
                description=description,
                current_quantity=current_quantity,
                quantity_threshold=quantity_threshold,
                metric=metric,
                created_at=created_at,
                supplier=supplier[0],
            )

            # instance.suppliers.add(*suppliers)
            
            return redirect(f"/inventory")

        except Exception as e:
            message = e
            # context = {'ingredients':ingredients, 'message':message}
            print(message)
            return render(request, 'ingredients/add_ingredient.html', context)

    else:
        return render(request, 'ingredients/add_ingredient.html', context)

def view_ingredient(request, pk):
    ingredient = get_object_or_404(Ingredient, pk=pk)
    if request.GET.get('message') == None:
        context = {"ingredient":ingredient}
    else:
        context = {"ingredient":ingredient, 'message':request.GET.get('message')}
    return render(request, 'ingredients/view_ingredient.html', context)