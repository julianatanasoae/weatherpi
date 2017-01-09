#!/usr/bin/env python
# Bring a json file down from the web.
# weatherjson.py
import urllib
 
api_url = "http://api.wunderground.com/api/7502edf0c2334475/conditions/q/Romania/Magurele.json"
 
urllib.urlretrieve(api_url, "/home/pi/weatherunderground.json")
