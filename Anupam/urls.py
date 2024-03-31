from django.urls import path
from . import views

urlpatterns=[
    path('',views.Home,name='home'),
    path('home/',views.Home,name='home'),
    path('analysis/',views.Welcome,name='analysis'),
    path('user/',views.User,name='user'),
    path('about/',views.About,name='about'),
    path('Departments/',views.Dept,name='dept'),
]
