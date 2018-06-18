from django.shortcuts import render
# Create your views here.


from django.http import HttpResponse


def home(request):
    return HttpResponse("Hello, World. You're at the Net life Home Page..")

def blog(request):
    return HttpResponse("This is the blog Page!")