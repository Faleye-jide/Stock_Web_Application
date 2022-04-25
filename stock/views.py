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
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LinearRegression
from keras.models import model_from_json
import pandas as pd 
import numpy as np
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

# @login_required(login_url='login')
def ticker(request, ticker_id): 
    context = {
        'ticker': ticker_id,
        'meta': get_data(ticker_id),
        'price': get_quote(ticker_id)
    }
    return render(request, 'stock/ticker.html', context)


def about(request):
    return render(request, 'stock/about.html', {})


# @login_required(login_url='login')
def get_news(request):
    # limit = '50'
    # token = 'b8mhjejpepKneMAMpIlDa4hniZeOHNhnbzZkF3P8'
    url = 'https://api.marketaux.com/v1/news/all?&exchanges=NYSE&filter_entities=true&published_after=2022-04-13T15:37&api_token=b8mhjejpepKneMAMpIlDa4hniZeOHNhnbzZkF3P8'
    r = requests.get(url)
    api = json.loads(r.content)

    '''
    api = r.json()
    print(api['data'])
    api_list = []
    for i in range(len(api['data'])):
        api_list.append(api['data'][i])
    print('list', api_list)
    context = {
         'api':api['data']
    }
    

    '''
    return render(request, 'stock/news.html', {'api':api})

def predict(request):
    
    # scale data 
    train_data = pd.read_csv('ml_model/Facebook_stock_price.csv')
    train = train_data.head(5)
    print(train)
    show ={
        'train':train
    }
    
    return render(request, 'stock/prediction.html', show)

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
            
            
def add_stock(request):
    if request.method == 'POST':
        form = TickerForm(request.POST or None)
        
        if form.is_valid():
            form.save()
            messages.success(request, 'Stock has been added to the portfolio')
            return redirect('add_stock')
        
    elif request.method == 'GET':
        ticker = stock.objects.all()
        resutl = []
        
        for tick in ticker:
            pass
                
            
        
    
def delete(request, stock_id):
    item = stock.objects.get(pk=stock_id) # fetch data from database by id
    item.delete()
    messages.success(request, 'Stock has been deleted successfully from the portfolio')   
    return redirect('add_stock')