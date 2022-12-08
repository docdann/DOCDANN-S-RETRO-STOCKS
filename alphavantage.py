import os

import requests


def time_series_intraday(symbol):
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={}&interval=5min&apikey={}' \
        .format(symbol, os.environ['AV_KEY'])
    r = requests.get(url)
    data = r.json()
    return data
def time_series_weekly(symbol):
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY&symbol={}&apikey={}'\
        .format(symbol, os.environ['AV_KEY'])
    r = requests.get(url)
    data = r.json()
    return data
def time_series_monthly(symbol):
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol={}&apikey={}'\
        .format(symbol, os.environ['AV_KEY'])
    r = requests.get(url)
    data = r.json()
    return data
