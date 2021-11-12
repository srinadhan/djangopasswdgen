from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.

def home(request):
    #return HttpResponse("hello there friend")
    return render(request,'generator/home.html',{'password':'test123'})

def about(request):
    #return HttpResponse("hello there friend")
    return render(request,'generator/about.html')

def eggs(request):
    return HttpResponse("<h1>Eggs are awesome</h1>")
def password(request):

    charecters = list('abcdefghijklmnopqrstuvwxyz')

    if (request.GET.get('uppercase')) :
        charecters.extend(list('ABCDEFGHIJLKMNOPQRSTUVWXYZ'))
    if (request.GET.get('special')) :
        charecters.extend(list('!@#$%^&*()'))
    if (request.GET.get('numbers')) :
        charecters.extend(list('0123456789'))

    length = int(request.GET.get('length',12))

    thepassword = ''

    for x in range(length):
        thepassword += random.choice(charecters)

    return render(request,'generator/password.html',{'password':thepassword})
