'''
Created on 2021-05-31

@author: Bartosz Walewski
'''
import requests
import json
from PyQt5 import QtGui

import data_operations

headers = {
        'x-rapidapi-key': "ENTER_KEY_HERE",
        'x-rapidapi-host': "weatherapi-com.p.rapidapi.com"
    }


def get_history_weather(date):
    url = "https://weatherapi-com.p.rapidapi.com/history.json"
    with open("current_city.json", "r") as read:
        city = json.load(read)
    querystring = {"q":city, "dt":date, "lang":"en"}
    try:
        response = requests.request("GET", url, headers=headers, params=querystring)
        return response.json()
    except:
        return None


def get_weather(query = "Opole"):
    query = data_operations.query_normalize(query)
    url = "https://weatherapi-com.p.rapidapi.com/forecast.json"
    querystring = {"q": query, "days": "3"}
    try:
        response = requests.request("GET", url, headers=headers, params=querystring)
        with open("current_weather.json", mode='w+') as put:
           put.write(json.dumps(response.json()))
        with open("current_city.json", mode='w+') as put:
           put.write(json.dumps(query))
        return response.json()
    except:
        return None


def search_localization(query):
    query = data_operations.query_normalize(query)
    url = "https://weatherapi-com.p.rapidapi.com/search.json"
    querystring = {"q": query}
    try:
        response = requests.request("GET", url, headers=headers, params=querystring)
        return response.json()
    except:
        return None


def get_icon(link):
    try:
        image = QtGui.QImage()
        image.loadFromData(requests.get(link).content)
        return image
    except:
        return None