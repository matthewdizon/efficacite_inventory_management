from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from ingredients.models import Ingredient
from django.contrib import messages
from django.forms.formsets import formset_factory, BaseFormSet
from .forms import ProductForm, ProductIngredientForm

def home(request):
    products = Product.objects.all()
    context = {"products":products}
    return render(request, 'products/index.html', context)

def add_product(request):
    ProductIngredientFormSet = formset_factory(ProductIngredientForm, formset=BaseFormSet)
    if(request.method=='POST'):
        product_form = ProductForm(request.POST)
        product_ingredient_formset = ProductIngredientFormSet(request.POST)

        if product_form.is_valid() and product_ingredient_formset.is_valid():
            product_name = product_form.cleaned_data.get('name')
            product_desc = product_form.cleaned_data.get('description')
            product_price = product_form.cleaned_data.get('price')
            
            product = Product.objects.create(
                name = product_name,
                description = product_desc,
                price = product_price,
            )

            product_ingredients = []
            for product_ingredient in product_ingredient_formset:
                ingredient = product_ingredient.cleaned_data.get('ingredient')
                qty = product_ingredient.cleaned_data.get('qty')
                product_ingredients.append(ProductIngredient(product=product, ingredient=ingredient, qty=qty))
            
            ProductIngredient.objects.bulk_create(product_ingredients)

    else:
        product_form = ProductForm()
        product_ingredient_formset = ProductIngredientFormSet()

    context = {
        'product_form': product_form,
        'product_ingredient_formset': product_ingredient_formset,
    }

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