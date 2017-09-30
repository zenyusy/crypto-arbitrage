# coding=utf-8
import requests

def crawl(url, return_type = 'text'):
    try:
        r = requests.get(url, timeout=5)
        r.raise_for_status()
        if return_type == 'text':
            return r.text
        else:
            return r.json()
    except:
        return ''
