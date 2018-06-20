from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name='Home'),
    path('blog/', views.blog, name='Blog'),
    path('myprojects/', views.projects, name='Projects'),
    path('about/', views.about, name='AboutMe'),
    path('feedback/', views.feedback, name='Feedback'),
]
