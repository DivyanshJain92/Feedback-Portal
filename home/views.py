from multiprocessing import context
from django.shortcuts import render , HttpResponse, redirect
from datetime import datetime,date
from home.models import Suggestion
from django.contrib import messages
from .models import Suggestion
from django.contrib.auth import authenticate, login

# Create your views here.

def index(request):
    return render(request,'index.html')

def feedback(request):
    if request.method =='POST':
        name = request.POST.get('name')
        des = request.POST.get('des')
        sugg = request.POST.get('sugg')
        opt = request.POST.get('opt')
        other = request.POST.get('other')
        suggestion = Suggestion(name=name,des=des,sugg=sugg,opt=opt)
        suggestion.save()
        messages.success(request, 'Feedback submitted sucessfully!')
    return render(request,'feedback.html')

def view(request):
    if request.user.isanonymous:
        return redirect("/login")
    data = Suggestion.objects.all()
    return render(request,'view.html',{'data':data})

def how(request):
    return render(request,'how.html')

def about(request):
    return render(request,'index.html')


def user_login(request):
    if request.method == 'POST':
        # Process the request if posted data are available
        username = request.POST['username']
        password = request.POST['password']
        # Check username and password combination if correct
        user = authenticate(username=username, password=password)
        if user is not None:
            # Save session as cookie to login the user
            login(request, user)
            # Success, now let's login the user.
            data = Suggestion.objects.all()
            return render(request,'view.html',{'data':data})
        else:
            # Incorrect credentials, let's throw an error to the screen.
            return render(request, 'login.html', {'error_message': 'Incorrect username and / or password.'})
    else:
        # No post data availabe, let's just show the page to the user.
        return render(request, 'login.html')

def logout(request):
     return render(request,'index.html')




# def service(request):
#     return HttpResponse("this is service")

# def contact(request):
#     return HttpResponse("this is contact")