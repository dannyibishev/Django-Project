from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name='Home'),
    path('blog/', views.blog, name='Blog'),
    path('feedback/', views.feedback, name='Feedback'),
]