#!/usr/bin/env python
import requests

url = "http://api.ipify.org"
resp = requests.get(url)
print(resp.text)

