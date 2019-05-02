#!/usr/bin/python
from scraper import ScrapeyWapey
import sys


# ref: https://towardsdatascience.com/how-to-web-scrape-with-python-in-4-minutes-bc49186a8460

sw = ScrapeyWapey

if len(sys.argv) <= 1:
    url = 'http://web.mta.info/developers/turnstile.html'
    # print ('You are using the default URL:\n' + url)
elif len(sys.argv) > 2:
    errormsg = 'Please pass none or 1 argument only'
    print(errormsg)
else:
    url = (sys.argv[1]).strip()
    # print ('The URL you have inputted is:\n' + url)


sw(url).Scrape(url)
