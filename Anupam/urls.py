from django.urls import path
from . import views

urlpatterns=[
    path('',views.Home,name='home'),
    path('home/',views.Home,name='home'),
    path('heart/',views.Welcome,name='heart'),
    path('liver/',views.Welcome,name='liver'),
    path('diabetes/',views.Welcome,name='diabetes'),
    path('cancer/',views.Welcome,name='cancer'),
    path('user/',views.User,name='user'),
    path('about/',views.About,name='about'),
    path('Departments/',views.Dept,name='dept'),
]
