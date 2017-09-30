# coding=utf-8
from utils import *

# return all tickers
def bithumb_tickers():
    dct = crawl('https://api.bithumb.com/public/ticker/ALL', 'json')['data']
    dct.pop('date') # keep only crypto info

    for k, v in dct.items():
        dct[k] = float(dct[k]['closing_price']) # keep only closing price
    return dct

def get_rate():
    from re import findall
    return float(findall(r'>[\d+\.]+', crawl('http://www.kuaiyilicai.com/uprate/krw.html'))[0][1:])

btc = bithumb_tickers()['BTC']
rate = get_rate()
