#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# XCoin API-call related functions
#
# Author: zenyu

import sys
if sys.version_info < (3, 0):
    sys.stdout.write("Sorry, this api requires Python 3.x\n")
    sys.exit(1)

import time
import base64
import hmac, hashlib
import json
from urllib import request, parse

class XCoinAPI:
    api_url = "https://api.bithumb.com";

    def __init__(self, pubkey, seckey):
        self.pubkey = pubkey;
        self.seckey = seckey;

    def xcoinApiCall(self, endpoint, rgParams):
        # 1. Api-Sign and Api-Nonce information generation.
        # 2. Request related information from the Bithumb API server.
        #
        # - nonce: it is an arbitrary number that may only be used once.
        # - api_sign: API signature information created in various combinations values.

        # add endpoint into the dict
        str_data = parse.urlencode(dict({"endpoint" : endpoint}, **rgParams))

        # in usec as a str
        nonce = str(int(time.time()*1000))

        data = chr(0).join((endpoint, str_data, nonce))

        # a lot of encoding conversions...
        h = hmac.new(self.seckey.encode('utf-8'), data.encode('utf-8'), hashlib.sha512);
        hex_output = h.hexdigest();
        utf8_hex_output = hex_output.encode('utf-8');
        api_sign = base64.b64encode(utf8_hex_output);
        utf8_api_sign = api_sign.decode('utf-8');

        r = request.urlopen(
                request.Request(self.api_url + endpoint,
                        data=str_data.encode('utf-8'),
                        headers={'Api-key': self.pubkey, 'Api-Sign': utf8_api_sign, 'Api-Nonce': nonce,}))
        return (json.loads(r.read().decode('utf-8')));
