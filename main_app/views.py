from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import User
from orders.models import Order
from django.core.mail import send_mail
from django.http import HttpResponse
from django.utils.dateparse import parse_date
from django.db.models import Sum, Count
import csv, datetime

def home(request):
    return render(request, 'main_app/index.html')

def login(request):
    if(request.method=="POST"):
        UN = request.POST.get('user')
        PW = request.POST.get('pass')
        
        if UN == "UserADMIN" and PW == "GRILLpass":
            return redirect('index') 
        else:
            messages.error(request,'Invalid Login Details')
            return redirect('login') 
    else:
        return render(request, 'main_app/sign_in.html')

def create_account(request):
    Acct=User.objects.all()
    if(request.method=="POST"):
        UN = request.POST.get('user')
        PW = request.POST.get('pass')
        fed=Acct.filter(username=UN, password=PW)
        try:    
            res=Acct.get(username=UN, password=PW)
            messages.error(request,'Account already exists')
            return render(request, 'main_app/create_account.html')
        except:
            messages.error(request,'Account Created Successfully')
            User.objects.create(username=UN, password=PW)
            return redirect('login')
    else:
        return render(request, 'main_app/create_account.html')

def export_salesreport(request):
    range_from = request.POST.get('range_from')
    range_to = request.POST.get('range_to')
    orders_by_ingredient = Order.objects.values_list('ingredient_order').filter(ordered_at__range=[range_from, str(parse_date(range_to)+datetime.timedelta(days=1))]).annotate(quantity=Sum('qty'), total=Sum('total')).order_by()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=sales_report.csv'

    writer = csv.writer(response)
    writer.writerow(['Ingredient', 'Quantity', 'Total'])
    for order in orders_by_ingredient:
        writer.writerow(order)
    return response