from django.shortcuts import render,HttpResponse
from datetime import datetime                    # we imported this
from home.models import Contact                 # and this
from django.contrib import messages

# Create your views here.
def index(request):
    # return HttpResponse('<h1>this is the home page</h1>')
    context={                                                  #context is the set of variables we send to templates
        "variable1":"KRATOS is the GOD OF WAR",                 # basically context is a dictionary  
        "variable2":"I am THE BEST IN THE WORLD"                     
    }
    return render(request,'index.html')

def about(request):
    #return HttpResponse('<h1>this is the about page</h1>')
    return render(request,'about.html')
def services(request):
    #return HttpResponse('<h1>this is the services page</h1>')
    return render(request,'services.html')

def contact(request):
    #return HttpResponse('<h1>this is the contact page</h1>')
    if request.method=="POST":                     #if some form is posted then this will run else next statement will execute 
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        Desc=request.POST.get('Desc')
        contact=Contact(name=name, email=email, phone=phone, Desc=Desc, date=datetime.today())
        contact.save()
        messages.success(request, 'You has been been submitted succesfully')
    
    return render(request,'contact.html')
