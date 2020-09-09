import requests
from django.shortcuts import render

def index(request):
    apiKey = "2bf2fb44f4864a15bf4c2f2b8ba92949"
    url = "http://newsapi.org/v2/top-headlines?country={}&category=health&apiKey=" + apiKey

    country = 'ru'
    res = requests.get(url.format(country)).json()

    health_news = {"articles" : res["articles"]}

    return render(request, 'dynamicdata/dypage.html', health_news)
