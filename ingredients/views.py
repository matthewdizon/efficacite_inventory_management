from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from suppliers.models import Supplier
from django.core.mail import send_mail

def home(request):
    ingredients = Ingredient.objects.all()
    context = {"ingredients":ingredients}
    return render(request, 'ingredients/index.html', context)

def send_notification(request):
    ingredients = Ingredient.objects.all()
    recipients = []
    context = {"ingredients":ingredients, "recipients":recipients}
    
    for x in ingredients:
        print(x.get_quantity_ratio())
        ratio = x.get_quantity_ratio()
        product = x.name
        email = x.supplier.getEmail()

        if ratio < 2:
            if ratio >= 1.5:
                title = f"Benjamin's Grill House | {product} Quantity: MEDIUM PRIORITY"
                body = f"{product} should be restocked soon. Current quantity left is: {x.current_quantity}. Our Quantity Threshold is: {x.quantity_threshold}"
            elif ratio < 1.5:
                title = f"Benjamin's Grill House | {product} Quantity: HIGH PRIORITY"
                body = f"{product} should be restocked immediately. Current quantity left is: {x.current_quantity}. Our Quantity Threshold is: {x.quantity_threshold}"

            # send_mail(
            # title, #Subject
            # body, #Body
            # 'grillhouseapp@gmail.com', #From
            # [email], #To
            # fail_silently=True,
            # )
            
            recipients.append([email, title, body])

    return render(request, 'ingredients/sent_mail.html', context)

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

def batch_ingredient(request, pk):
    ingredient = get_object_or_404(Ingredient, pk=pk)
    Quantity = ingredient.current_quantity
    if(request.method=="POST"):
        batchq = request.POST.get('batch_quantity')
        newquantity = int(batchq) + int(Quantity)
        #try: 
        #    Ingredient.objects.get(name=foodname)
        #    messages.error(request,'Food already exist')
        #    return redirect('view_food')
        #except:
        Ingredient.objects.filter(pk=pk).update(current_quantity = str(newquantity))
        return redirect('ingredient_index')
    else:
        return render(request, 'ingredients/batch_ingredient.html', {'ingredient':ingredient})

def view_ingredient(request, pk):
    ingredient = get_object_or_404(Ingredient, pk=pk)
    if request.GET.get('message') == None:
        context = {"ingredient":ingredient}
    else:
        context = {"ingredient":ingredient, 'message':request.GET.get('message')}
    return render(request, 'ingredients/view_ingredient.html', context)