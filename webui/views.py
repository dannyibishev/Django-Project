from django.shortcuts import render
# from django.template import loader
# Create your views here.


from django.http import HttpResponse

APP_TITLE = 'NetLife'

# Normal HTML Requests
def home(request):
    context = {'app_title': APP_TITLE}
    return render(request, 'structure/home.html')


def blog(request):
    context = {'app_title': APP_TITLE}
    return render(request, 'structure/blog.html')


def about(request):
    context = {'app_title': APP_TITLE}
    return render(request, 'structure/devinfo.html')


def projects(request):
    context = {'app_title': APP_TITLE}
    return render(request, 'structure/myprojects.html')


# APP Functionality
def feedback(request):
    return HttpResponse("Thank you for your feedback. Back to Home.")

