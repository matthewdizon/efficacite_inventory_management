from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from suppliers.models import Supplier
# from ingredients.models import Ingredient
from products.models import Product
from django.contrib import messages

def home(request):
    orders = Order.objects.all()
    context = {"orders":orders}
    return render(request, 'orders/index.html', context)


def add_order(request):
    if(request.method=="POST"):
        order_objects = Order.objects.all()
        # try:
        #     product = Product.objects.get(name=request.POST.get('o_food'))
        #     qty = request.POST.get('o_quantity')
        #     payment = request.POST.get('o_pmode')
        #     # orderedat = request.POST.get('o_orderedat')
        #     status = request.POST.get('o_status')
        #     Order.objects.create(ingredient_order= ingredient, qty=qty, payment_mode=payment, status=status)
        #     new_qty = int(ingredient.current_quantity) - int(qty)
        #     product.current_quantity = new_qty
        #     product.save()
        #     return redirect(f"/orders")
        try:
            product = Product.objects.get(name=request.POST.get('o_food'))
            qty = request.POST.get('o_quantity')
            payment = request.POST.get('o_pmode')
            # orderedat = request.POST.get('o_orderedat')
            status = request.POST.get('o_status')
            print(product.getName())
            # print(product.ingredients.all())
            for i in product.ingredients.all():
                print(i.name, i.current_quantity)
            # product.current_quantity = new_qty
            # product.save()
            return redirect(f"/orders")
        except:
            messages.error(request, 'Please complete Order details!')
            i = Product.objects.all()
            return render(request, 'orders/add_order.html', {'products':i})
    
    else:
        i = Product.objects.all()
        return render(request, 'orders/add_order.html', {'products':i})

def update_order(request, pk):
    o = get_object_or_404(Order, pk=pk)
    # o_qty = request.POST.get('qty')
    o_status = request.POST.get('status')
    order_objects = Order.objects.all()

    if(request.method=="POST"):
        # Order.objects.filter(pk=pk).update(qty = o_qty, status = o_status)
        Order.objects.filter(pk=pk).update(status = o_status)
        return redirect(f"/orders")

    else:
        return render(request, 'orders/update_order.html', {'o': o})

def delete_order(request, pk):
    order = Order.objects.get(pk=pk)
    order.delete()
    return redirect(f"/orders")

from django.views.generic import ListView, TemplateView
from .forms import OrderFormSet
from django.urls import reverse_lazy
from django.shortcuts import redirect

class OrderAddView(TemplateView):
    template_name = "orders/add_order.html"

    def get(self, *args, **kwargs):
        formset = OrderFormSet(queryset=Order.objects.none())
        return self.render_to_response({'order_formset': formset})

    # Define method to handle POST request
    def post(self, *args, **kwargs):

        formset = OrderFormSet(data=self.request.POST)

        # Check if submitted forms are valid
        if formset.is_valid():
            for f in formset:
                cd = f.cleaned_data
                qty = cd['qty']
                print("cd", cd)
                print("qty", qty)
                ingredient = cd['ingredient_order']
                print("ingredient", ingredient)
                new_qty = int(ingredient.current_quantity) - int(qty)
                ingredient.current_quantity = new_qty
                ingredient.save()

            formset.save()
            return redirect(reverse_lazy("add_order"))

        return self.render_to_response({'order_formset': formset})
