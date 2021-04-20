from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth, messages
# Create your views here.

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user = auth.authenticate(username= username, password= password)

        if user is not None:
            auth.login(request, user)
            messages.add_message(request,messages.SUCCESS,"Oturum acma basarili")
            return redirect('movies')
        else:  
            messages.add_message(request, messages.ERROR,"Oturum acma basarisiz")
            return redirect('login')

    else:
        return render(request,"user/login.html")


def register(request):
    if request.method == 'POST':
        #get form values
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        repassword = request.POST['repassword']

        if password == repassword:
            # Username control
            if User.objects.filter(username= username).exists():
                messages.add_message(request,messages.WARNING,"Bu kullanici ad daha once alinmistir")
                return redirect('register')
            
            else:
                if User.objects.filter(email= email).exists():
                    messages.add_message(request,messages.WARNING,"Bu email daha once alinmistir")
                    return redirect('register')

                else:
                    # her sey guzel 
                    # kayit islemi yapilabilir
                    user=User.objects.create_user(username=username, email=email, password=password)
                    user.save()
                    messages.add_message(request,messages.SUCCESS,"Kullanici olusturma islemi basarili")
                    return redirect('login')
        else:
            messages.add_message(request,messages.WARNING,"Parolalar eslesmiyor")
            return redirect('register')
    else:
        return render(request,"user/register.html")



def logout(request):
    if request.method=="POST":
        auth.logout(request)
        messages.add_message(request,messages.SUCCESS,"Cikis islemi basarili")
        return redirect('movies')
