#! /usr/bin/env python3
# XCoin API-call sample script (for Python 3.X)
#
# @author	btckorea
# @date	2017-04-11

from xcoin_api_client import *


api_key = "api_connect_key";
api_secret = "api_secret_key";

api = XCoinAPI(api_key, api_secret);

rgParams = {
	"order_currency" : "BTC",
	"payment_currency" : "KRW"
};


#
# public api
#
# /public/ticker
# /public/recent_ticker
# /public/orderbook
# /public/recent_transactions

result = api.xcoinApiCall("/public/ticker", rgParams);
print("status: " + result["status"]);
print("last: " + result["data"]["closing_price"]);
print("sell: " + result["data"]["sell_price"]);
print("buy: " + result["data"]["buy_price"]);


#
# private api
#
# endpoint		=> parameters
# /info/current
# /info/account
# /info/balance
# /info/wallet_address

#result = api.xcoinApiCall("/info/account", rgParams);
#print("status: " + result["status"]);
#print("created: " + result["data"]["created"]);
#print("account id: " + result["data"]["account_id"]);
#print("trade fee: " + result["data"]["trade_fee"]);
#print("balance: " + result["data"]["balance"]);
