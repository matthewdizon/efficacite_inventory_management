from django.shortcuts import render, redirect, get_object_or_404
from .models import *

def home(request):
    products = Product.objects.all()
    context = {"products":products}
    return render(request, 'products/index.html', context)

def add_product(request):
    if(request.method=="POST"):
        product_name = request.POST.get('product_name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        created_at = request.POST.get('date')
        
        try:
            Product.objects.create(
                name=product_name,
                description=description,
                price=price,
                created_at=created_at,
            )

            # message="Product created successfully"
            # return redirect(f"/foods?message={message}")
            return redirect(f"/products")

        except Exception as e:
            message = e
            context = {'message':message}
            print(context)
            return render(request, 'products/add_product.html', context)

    else:
        return render(request, 'products/add_product.html')
    
def view_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.GET.get('message') == None:
        context = {"product":product}
    else:
        context = {"product":product, 'message':request.GET.get('message')}
    return render(request, 'products/view_product.html', context)

def update_product(request, pk):
    o = get_object_or_404(Order, pk=pk)
    o_qty = request.POST.get('qty')
    o_pmethod = request.POST.get('pmethod')
    order_objects = Order.objects.all()
    account_objects = Account.objects.all()


    if(request.method=="POST"):
        Order.objects.filter(pk=pk).update(qty = o_qty, payment_mode = o_pmethod)
        return render(request, 'GrabGrub_App/order_list.html', {'order':order_objects, 'accounts':account_objects})

    else:
        return render(request, 'GrabGrub_App/update_order.html', {'o': o})