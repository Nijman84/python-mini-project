#!/usr/bin/python3
import json as j
import csv
import errno
from urllib import request as u
from os import remove

'''
This is Alteryx community challenge 7:
https://community.alteryx.com/t5/Weekly-Challenge/Challenge-7-Download-Data-and-Parse-JSON/td-p/36734

API:
https://www.quandl.com/api/v3/datasets/UTOR/TOR_USA.json?api_key=5aMivNdsRkZNB-afkjse

Quandl is a search engine for numerical data.
The site offers access to several million financial, economic and social datasets.
Quandl indexes data from multiple sources allowing users to find and download in various formats.
All Quandl's data are accessible via an API.
For this example the response from these APIs is JSON.
Our user is trying to get aggregated Annual Outbound Tourism Statistics for the US dating back to 1995.
The Text Input contains the URL for the API request. Your goal is to parse the response.

Hint:  After parsing the JSON, you will need to further
identify the patterns within the data to effectively stage
into a table for analytics.
'''

# This section is for parsing straight from the API i.e. traveldata.json not saved
base_url = 'https://www.quandl.com/api/v3/datasets/UTOR/TOR_USA.json'
api_key = '5aMivNdsRkZNB-afkjse'
url = base_url + '?api_key=' + api_key

print("Parsing JSON from: " + base_url)
response = u.urlopen(url)

'''
# To bypass the API call, use this section to get the data from file
print("Parsing JSON from local JSON file)
response = open('traveldata.json')
'''

data = j.loads(response.read())
outputfile = 'challenge_07.csv'


def silentremove(filename):
    try:
        remove(filename)
    except OSError as e:
        if e.errno != errno.ENOENT:
            raise


silentremove(outputfile)

columns = data['dataset']['column_names']

with open(outputfile, 'w') as csvFile:
    wr = csv.writer(csvFile, dialect='excel', quoting=csv.QUOTE_NONNUMERIC)
    wr.writerow(columns)
csvFile.close()

csvBody = data['dataset']['data']

csvData = open(outputfile, 'a')
csvwriter = csv.writer(csvData)
for el in csvBody:
    csvwriter.writerow(el)
csvData.close()

print('Your parsed JSON has been outputted to: ' + outputfile)
