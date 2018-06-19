from django.shortcuts import render
# from django.template import loader
# Create your views here.


from django.http import HttpResponse

APP_TITLE = 'NetLife'

def home(request):
    context = {'title': APP_TITLE}
    return render(request, 'index.html')


def blog(request):
    return HttpResponse("This is the blog Page!")


def feedback(request):
    return HttpResponse("Thank you for your feedback. Back to Home.")

