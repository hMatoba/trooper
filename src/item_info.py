import os
import urllib.request
import json

url = 'https://shopping.yahooapis.jp/ShoppingWebService/V3/itemSearch'

def get_item_info(jan_code):
    if jan_code[0] != '4':
        return None

    params = {
        'appid': os.environ['YJ_CLIENT_ID'],
        'jan_code': jan_code,
        'sort': '-sold',
    }

    req = urllib.request.Request('{}?{}'.format(url, urllib.parse.urlencode(params)))
    with urllib.request.urlopen(req) as res:
        json_body = res.read().decode('utf8')
        body = json.loads(json_body)

    if not('hits' in body) or len(body['hits']) == 0:
        return None

    return body['hits'][0]['name']
