from django.shortcuts import render

from .models import Contact,Course

# Create your views here.

def mainhome(request):
    return render(request,'mainhome.html')

def signin(request):
    return render(request,'signin.html')

def signup(request):
    return render(request,'signup.html')

def forgot(request):
    return render(request,'forgot.html')

def course(request):
    courses={
        'course':Course.objects.all()
    }
    return render(request,'course.html',courses)

def gallery(request):
    return render(request,'gallery.html')

def contact(request):
    if request.method=="POST":
        if request.POST['name']is not None:
            enq=Contact.objects.create(name=request.POST['name'],email=request.POST['email'],phno=request.POST['phno'])
            enq.save()
            # message.success(request,'contact-soon')
            dicts={'out':1,'name':request.POST['name']}
            return render(request,'contact.html',dicts)
    return render(request,'contact.html')
