from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('<str:ticker_id>', views.ticker, name='ticker'),
]
