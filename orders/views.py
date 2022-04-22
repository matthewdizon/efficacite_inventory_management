from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from suppliers.models import Supplier
from ingredients.models import Ingredient
from django.contrib import messages

def home(request):
    orders = Order.objects.all()
    context = {"orders":orders}
    return render(request, 'orders/index.html', context)


def add_order(request):
    if(request.method=="POST"):
        order_objects = Order.objects.all()
        try:
            ingredient = Ingredient.objects.get(name=request.POST.get('o_food'))
            qty = request.POST.get('o_quantity')
            payment = request.POST.get('o_pmode')
            orderedat = request.POST.get('o_orderedat')
            status = request.POST.get('o_status')
            Order.objects.create(ingredient_order= ingredient, qty=qty, ordered_at=orderedat, payment_mode=payment, status=status)
            #ingredient.update(current_quantity=ingredient.current_quantity - qty)
            return render(request, 'orders/index.html', {'order':order_objects})
        except:
            messages.error(request, 'Please complete Order details!')
            i = Ingredient.objects.all()
            return render(request, 'orders/add_order.html', {'ingredients':i})
    
    else:
        i = Ingredient.objects.all()
        return render(request, 'orders/add_order.html', {'ingredients':i})

def update_order(request, pk):
    o = get_object_or_404(Order, pk=pk)
    o_qty = request.POST.get('qty')
    o_status = request.POST.get('status')
    order_objects = Order.objects.all()

    if(request.method=="POST"):
        Order.objects.filter(pk=pk).update(qty = o_qty, status = o_status)
        return render(request, 'orders/index.html', {'order':order_objects})

    else:
        return render(request, 'orders/update_order.html', {'o': o})