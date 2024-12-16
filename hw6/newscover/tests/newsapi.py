import unittest
from requests import HTTPError
import newscover.newsapi as na
import json
from datetime import datetime, timedelta

with open('~/hw6/newscover/tests/test_secrets.json') as f:
    secrets = json.load(f)
API_KEY = secrets['api_key']

class TestNewsAPI(unittest.TestCase):
    # makes sure query with no keywords raises error
    def test_noKeywords(self):
        with self.assertRaises(HTTPError):
            na.fetch_latest_news(API_KEY,[])

    # makes sure lookback works properly
    def test_lookback(self):
        # helper function to test if lookback date works
        def tester(days, keys):
            articles = na.fetch_latest_news(API_KEY, keys, days)
            date = (datetime.today() - timedelta(days=days)).replace(microsecond=0)
            for cur in articles:
                cur_date = datetime.fromisoformat(cur['publishedAt'])
                if (cur_date < date) :
                    return False
            return True
        
        self.assertTrue(tester(5, ['Biden']))
        self.assertTrue(tester(9, ['Trump', 'Harris']))

    # makes sure non alphabetical keywords throw an error
    def test_NonAlpha(self):
        with self.assertRaises(HTTPError):
            na.fetch_latest_news(API_KEY, ["4*&29q"])

if __name__ == '__main__':
    unittest.main()