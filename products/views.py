from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from ingredients.models import Ingredient

def home(request):
    products = Product.objects.all()
    context = {"products":products}
    return render(request, 'products/index.html', context)

def add_product(request):
    ingredients_objects = Ingredient.objects.all()
    context = {'ingredients':ingredients_objects}
    
    if(request.method=="POST"):
        product_name = request.POST.get('product_name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        created_at = request.POST.get('date')
        ingredient_ids = request.POST.getlist('ingredients')
        
        ingredients = Ingredient.objects.filter(pk__in=ingredient_ids)
        print(ingredients)

        try:
            instance = Product.objects.create(
                name=product_name,
                description=description,
                price=price,
                created_at=created_at,
            )
            
            instance.ingredients.add(*ingredients)

            # message="Product created successfully"
            # return redirect(f"/foods?message={message}")
            return redirect(f"/products")

        except Exception as e:
            message = e
            context = {'ingredients':ingredients_objects, 'message':message}
            print(context)
            return render(request, 'products/add_product.html', context)

    else:
        return render(request, 'products/add_product.html', context)
    
def view_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.GET.get('message') == None:
        context = {"product":product}
    else:
        context = {"product":product, 'message':request.GET.get('message')}
    return render(request, 'products/view_product.html', context)

def update_product(request, pk):
    
    if(request.method=="POST"):
        try:
            prodname = request.POST.get('proname')
            proddesc = request.POST.get('prodesc')
            prodprice = request.POST.get('proprice')
            proddate = request.POST.get('prodate')
            prod = get_object_or_404(Product, pk=pk)
            Product.objects.filter(pk=pk).update(name=prodname, description=proddesc, price=prodprice, created_at=proddate)
            return redirect('view_product', pk=pk)
        except:
            messages.error(request, 'Please update the details!')
            context = {"product":prod}
            return render(request, 'products/update_product.html', context)

    else:
        prod = get_object_or_404(Product, pk=pk)
        context = {"product":prod}
        return render(request, 'products/update_product.html', context)

def delete_product(request, pk):
    product = Product.objects.get(pk=pk)
    product.delete()
    return redirect(f"/products")