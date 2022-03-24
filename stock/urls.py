from django.urls import path
from . import views


# app_name = 'stock'

urlpatterns = [
    path('',views.home, name='home'),
    path('register', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('<str:ticker_id>', views.ticker, name='ticker'),
]
