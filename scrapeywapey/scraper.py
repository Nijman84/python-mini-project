import requests
import urllib.request
import time
from bs4 import BeautifulSoup


class ScrapeyWapey:
    '''
    Scrape data from New York Metro sit for station usage
    '''
    def __init__(self, url):
        self.url = url

    def Scrape(self, url):
        print ('Parsed URL: ' + url)
        # Check that you get a 200 html response
        response = requests.get(url)
        print (response)
        # Soup to parse in the website into a list
        soup = BeautifulSoup(response.text, 'html.parser')
        # Filter out all the html <a> tags
        all_a = soup.findAll('a')
        print(all_a)
# Choose an <a> ref with link to a text file for downloading data file
# one_a_tag = all_a[64]
#
# # Extract the actual link element of the <a> link from above
# link = one_a_tag['href']
#
# # Generate absolute download URL, not relative
# download_url = 'http://web.mta.info/developers/' + link
# print(download_url)
#
# # Execute the download, with the file being placed into ./rawdata/ directory
# urllib.request.urlretrieve(download_url, './rawdata/'+link[link.find('/turnstile_')+1:])
#
# # This is for when we put it all in to a for loop to download all the data
# time.sleep(1)
