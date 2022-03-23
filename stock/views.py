from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import TickerForm
from django.http import HttpResponseRedirect
from .stockApi import get_data, get_quote

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
