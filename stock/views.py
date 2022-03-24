from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from .forms import TickerForm, NewUserForm
from django.http import HttpResponseRedirect
from .stockApi import get_data, get_quote
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

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

def ticker(request, ticker_id): 
    context = {
        'ticker': ticker_id,
        'meta': get_data(ticker_id),
        'price': get_quote(ticker_id)
    }
    return render(request, 'stock/ticker.html', context)

def register(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful')
            return redirect('login')
        messages.error(request, 'Registration Unsuccessful')
    # if it is a GET request
    # create a blank form 
    form = NewUserForm()
    return render(request, 'stock/register.html', context={'RegisterForm':form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                messages.info(request, f'You are logged in {username}')
                return redirect('home')
            else:
                messages.error(request, 'Invalid username or password')
        else:
            messages.error(request, 'Invalid username or password')
    form = AuthenticationForm()
    context = {
        'loginForm':form
    }
    return render(request, 'stock/login.html', context=context)

def logout_view(request):
    logout(request)
    messages.info("you are logged out successfully")
    return redirect('home')
            
            
                