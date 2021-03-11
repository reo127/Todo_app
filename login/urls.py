
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.homePage, name='homePage'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('signup/', views.HandleSignup, name='HandleSignup'),
    path('login/', views.HandleLogin, name='HandleLogin'),
    path('logoutHandle/', views.logoutHandle, name='logoutHandle'),
]
