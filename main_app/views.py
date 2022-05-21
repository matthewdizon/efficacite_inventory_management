from django.shortcuts import render #, redirect, get_object_or_404
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import User
from django.core.mail import send_mail

def home(request):
    return render(request, 'main_app/index.html')

def login (request):
    if(request.method=="POST"):
        UN = request.POST.get('user')
        PW = request.POST.get('pass')
        
        #if User.objects.filter(username = UN, password = PW):
            #acc = get_object_or_404(User, username = UN, password = PW )
            #return render(request, 'main_app/index.html')
        if UN == "UserADMIN" and PW == "GRILLpass":
            send_mail(
            'Test email',
            'Test Email for the app ',
            'grillhouseapp@gmail.com',
            ['gerard.aaron.tan@obf.ateneo.edu'],
            fail_silently=False,
                    )
            return render(request, 'main_app/index.html')
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