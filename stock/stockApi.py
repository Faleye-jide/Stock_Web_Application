import requests
import pandas as pd
# import matplotlib.pyplot as plt
import datetime


# get the data

headers  = {
    'Content-Type': 'application/json',
    'Authorization' : 'Token 42195f14d67b77ab93788c8c4e93f21b204ab171'
}


ticker_list = ['MSFT', 'FB', 'AAPL', 'AMZN', 'GOOG', 'JPM', 'TSLA']
api = '42195f14d67b77ab93788c8c4e93f21b204ab171'


# get the ticker
def get_data(ticker):
    url = f'https://api.tiingo.com/tiingo/daily/{ticker}'
    response = requests.get(url, headers=headers).json()
    # print(response)
    return response

    
# get the price 
def get_quote(ticker):
    url = 'https://api.tiingo.com/tiingo/daily/{}/prices'.format(ticker)
    response = requests.get(url, headers=headers).json()
    return response[0]
    
    
def news(request):
    pass


