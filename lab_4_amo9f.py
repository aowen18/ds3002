#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 18:50:44 2022

@author: alexaowen
"""

import json
import requests
import sys

url = "https://yfapi.net/v6/finance/quote"

stocks = sys.argv[1]

querystring = {"symbols":sys.argv[1]}
headers = {
    'x-api-key':'d5mT43gLG0azZGwFTo2E226H4e5yFmiI6sT14yy7'
    }
response = requests.request("GET", url, headers=headers, params=querystring)
info = json.loads(response.text)
try:
    name = info['quoteResponse']['result'][0]["longName"]
    price = info['quoteResponse']['result'][0]["regularMarketPrice"]
    print (name, ":", price)
except IndexError:
    print ("Error: Stock Not Found")