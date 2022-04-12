from django.urls import path
from . import views


# app_name = 'stock'

urlpatterns = [
    path('',views.home, name='home'),
    path('register', views.register, name='register'),
    path('about', views.about, name='about'),
    path('news', views.get_news, name='news'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('<str:ticker_id>', views.ticker, name='ticker'),
]
