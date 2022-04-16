from django.shortcuts import render #, redirect, get_object_or_404
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
            ingredient_id = request.POST.get('o_food')
            print(ingredient_id)

            ingredient = Ingredient.objects.filter(pk=ingredient_id)
            print(ingredient)
            qty = request.POST.get('o_quantity')
            payment = request.POST.get('o_pmode')
            orderedat = request.POST.get('o_orderedat')
            status = request.Post.get('o_status')
            Order.objects.create(ingredient_order= ingredient_id, qty=qty, payment_mode=payment, ordered_at=orderedat, status=status)
            #ingredient.update(current_quantity=ingredient.current_quantity - qty)
            return render(request, 'orders/order_list.html', {'order':order_objects})
        except:
            messages.error(request, 'Please complete Order details!')
            i = Ingredient.objects.all()
            return render(request, 'orders/add_order.html', {'ingredients':i})
    
    else:
        i = Ingredient.objects.all()
        return render(request, 'orders/add_order.html', {'ingredients':i})
