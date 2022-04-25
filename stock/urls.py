from django.urls import path
from . import views


# app_name = 'stock'

urlpatterns = [
    path('',views.home, name='home'),
    path('register', views.register, name='register'),
    path('about', views.about, name='about'),
    path('news', views.get_news, name='news'),
    path('prediction', views.predict, name='prediction'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('add_stock/', views.add_stock, name='add_stock'),
    path('<str:ticker_id>', views.ticker, name='ticker'),
]
