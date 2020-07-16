from django.shortcuts import render,HttpResponse

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
    return render(request,'contact.html')
