from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('cdc', views.cdc, name='cdc'),
    path('login', views.loginPage, name ="login"),
    path('signup', views.registerPage , name ="signup"),
    path('logout', views.logoutUser , name ="logout"),
    path('user', views.DataAdder, name='user'),
    path('viewer', views.DataViewer, name='viewer'),
    path('fullpost/<str:title>/',views.FullPost,name='fullpost'),
    path('invest_now/<str:user>/', views.invest_now_view, name='invest_now'),
    path('edit',views.profile,name='edit')
    ####
    # path('viewer', views.DataViewer, name='viewer'),
    
    
]