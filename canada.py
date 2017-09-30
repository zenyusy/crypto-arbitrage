# coding=utf-8
from utils import *

def btc_ticker():
    dct = crawl('https://api.cbix.ca/v1/index', 'json')
    # TODO
    # 'https://www.canadianbitcoins.com/index.php?currency=BTC'
    return max(map(lambda w: float(w['bid']), dct['exchanges']))

def get_rate():
    from re import findall
    return float(findall(r'CAD = \d\.\d+', crawl('http://www.everforex.ca/cn/rate/RtCalc.aspx?p=CADRMB'))[0][6:])

btc = btc_ticker()
rate = get_rate()
