#!/usr/bin/python3
import requests_oauthlib
import requests
# from os import remove
# import errno
import json
import sys
sys.path.insert(0, '/Users/nijman84/dev/python-mini-project/')
from myfuncs import silentremove # noqa


print(sys.path)

if len(sys.argv) <= 1:
    print('Please specify a twitter handle to scrape as the 1st argument')
    print('Additionally, please specify your twitter credentials as the subsequent arguments')
    exit(1)

screen_name = sys.argv[1]
record_no = 200
max_id = 200
api_key = sys.argv[2]
api_secret = sys.argv[3]
access_token = sys.argv[4]
access_token_secret = sys.argv[5]
output_json_file = './json_response.json'
outputfile = screen_name + '_data.csv'
auth = requests_oauthlib.OAuth1(api_key, api_secret, access_token, access_token_secret)
# url = 'https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name={}&count={}&max_id={}'.format(screen_name, record_no, max_id)
url = 'https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name={}&count={}'.format(screen_name, record_no)
print('url is: ', url)

r = requests.get(url, auth=auth)
print ('API Response: ', r)

data = json.loads(r.text)

silentremove(output_json_file)

with open(output_json_file, 'w') as f:
    json.dump(data, f)
f.close()

silentremove(outputfile)

with open(outputfile, 'w') as f:
    for i in range(len(data)):
        row = i + 1
        cr_dt = data[i]['created_at']
        try:
            user_mentions = str(data[i]['entities']['user_mentions'][0]['screen_name']) or ''
        except IndexError:
            user_mentions = 'N/A'
        row_string = '{0}, "{1}", "{2}"\n'.format(row, cr_dt, user_mentions)
        f.write(row_string)
f.close()
