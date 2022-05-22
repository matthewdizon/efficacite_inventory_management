from django.shortcuts import render
from typing import NoReturn
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import *
# Create your views here.

def home(request):
    Suppliers = Supplier.objects.all()
    context = {"Suppliers":Suppliers}
    return render(request, 'suppliers/index.html', context)

def supplier_entry(request):
    if(request.method=="POST"):
        Sname = request.POST.get('Sname')
        Saddress = request.POST.get('Saddress')
        Sphonenumber =  request.POST.get('Sphonenumber')
        Semailaddress = request.POST.get('Semailaddress')
        """
        try: 
            Supplier.objects.get(name=Sname)
            messages.error(request,'Supplier already exist')
            return redirect(f"/suppliers")
        except:
            Supplier.objects.create(name= Sname, 
            address= Saddress, 
            phonenumber= Sphonenumber,
            emailaddress = Semailaddress,
            )
            return redirect(f"/suppliers")
        """
        Supplier.objects.create(name= Sname, address= Saddress, phonenumber= Sphonenumber,emailaddress = Semailaddress)
        return redirect(f"/suppliers")

    else:        
       return render(request, 'suppliers/add_supplier.html')

def view_supplier(request, pk):
    supplier = get_object_or_404(Supplier, pk=pk)
    if request.GET.get('message') == None:
        context = {"supplier":supplier}
    else:
        context = {"supplier":supplier, 'message':request.GET.get('message')}
    return render(request, 'suppliers/view_supplier.html', context)

def update_supplier(request, pk):
    
    if(request.method=="POST"):
        try:
            Sname = request.POST.get('Sname')
            Saddress = request.POST.get('Saddress')
            Sphonenumber =  request.POST.get('Sphonenumber')
            Semailaddress = request.POST.get('Semailaddress')
            supp = get_object_or_404(Supplier, pk=pk)
            Supplier.objects.filter(pk=pk).update(name=Sname, address=Saddress, phonenumber=Sphonenumber, emailaddress=Semailaddress)
            return redirect('view_supplier', pk=pk)
        except:
            messages.error(request, 'Please update the details!')
            context = {"supplier":supp}
            return render(request, 'suppliers/update_supplier.html', context)

    else:
        supp = get_object_or_404(Supplier, pk=pk)
        context = {"supplier":supp}
        return render(request, 'suppliers/update_supplier.html', context)

def delete_supplier(request, pk):
    supplier = Supplier.objects.get(pk=pk)
    supplier.delete()
    return redirect(f"/supplier")