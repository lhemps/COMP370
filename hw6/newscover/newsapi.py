import requests
from datetime import datetime, timedelta

NEWS_URL = "https://newsapi.org/v2/everything?"

def fetch_latest_news(api_key, news_keywords, lookback_days=10):
    for word in news_keywords:
        if  not word.isalpha():
            raise requests.HTTPError()
    query = "q=" + ' AND '.join(news_keywords)
    lookback = datetime.today() - timedelta(days=lookback_days)
    lookback = lookback.replace(microsecond=0).isoformat()
    url = NEWS_URL + query + '&from=' + lookback + '&language=en' + '&apiKey=' + api_key
    
    response = requests.get(url)
    response.raise_for_status()
    articles = response.json()['articles']

    return articles