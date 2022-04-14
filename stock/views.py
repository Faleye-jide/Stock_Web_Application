from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render, get_object_or_404
from .forms import TickerForm, NewUserForm
# from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from .stockApi import get_data, get_quote
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .models import stock
from django.contrib.auth.decorators import login_required
import json
import requests


# Create your views here.
def home(request):
    if request.method == 'POST':
        form = TickerForm(request.POST)
        if form.is_valid():
            ticker = request.POST['ticker']
            return HttpResponseRedirect(ticker)
    else:
        form = TickerForm()
    return render(request, 'stock/home.html', {'form':form})

@login_required(login_url='login')
def ticker(request, ticker_id): 
    context = {
        'ticker': ticker_id,
        'meta': get_data(ticker_id),
        'price': get_quote(ticker_id)
    }
    return render(request, 'stock/ticker.html', context)


def about(request):
    return render(request, 'stock/about.html', {})


@login_required(login_url='login')
def get_news(request):
    url = 'https://stocknewsapi.com/api/v1/category?section=alltickers&items=50&token=myrtchxv2dwwls1qr1cia9w0d3fn0jku9x3a9aht'
    api_request = requests.get(url)
    api = json.loads(api_request.content)
    # print('here', api)
    context = {
        'api':api
    }
    return render(request, 'stock/news.html', context)

# def news(request, ticker_id):
#     context = {
#         'news': get_news(ticker_id)
#     }
#     return render(request, 'stock/news.html', context)


def register(request):
    # if request.user.is_authenticated:
    #     return redirect('home')
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')
            
            messages.success(request, 'Registration successful')
            # return redirect('login')
        else:
            return render(request, 'stock/register.html', {'RegisterForm': form})
        # messages.error(request, 'Registration Unsuccessful')
    # if it is a GET request
    # create a blank form 
    else:
        form = NewUserForm()
        return render(request, 'stock/register.html', context={'RegisterForm':form})

def login_view(request):
    if request.user.is_authenticated:
        return render(request, 'stock/home.html')
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            print(f'USER: {user}')
            if user:
                login(request, user)
                messages.info(request, f'You are logged in {username}')
                return redirect('home')
            else:
                messages.error(request, 'Invalid username or password')
                return redirect ('login')
        else:
            messages.error(request, 'Invalid username or password')
    
    form = AuthenticationForm()
    context = {
        'loginForm':form
    }
    return render(request, 'stock/login.html', context=context)

def logout_view(request):
    logout(request)
    messages.info(request, "you are logged out successfully")
    return redirect('home')
            
            
                