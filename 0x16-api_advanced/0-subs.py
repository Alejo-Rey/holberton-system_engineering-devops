#!/usr/bin/python3
""" fetch a page reddit to get  the subcribers """
import requests


def number_of_subscribers(subreddit):
    """ function to get the subcribers """
    url = 'https://www.reddit.com/r/' + subreddit + '/about.json'
    headers = {"User-Agent":
               "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0)\
               Gecko/20100101 Firefox/69.0"}
    req = requests.get(url, headers=headers, allow_redirects=False)
    if req.status_code == 200:
        return req.json().get('data').get('subscribers')
    return 0
