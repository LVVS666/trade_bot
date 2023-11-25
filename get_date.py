import datetime
import json
import hmac
import base64
import requests


def get_time():
    now = datetime.datetime.utcnow()
    t = now.isoformat("T", "milliseconds")
    return t + "Z"


def signature(timestamp, request_type, endpoint, body, secret):
    if body != '':
        body = json.dumps(body)
    message = str(timestamp) + str.upper(request_type) + endpoint + body
    print(message)
    mac = hmac.new(bytes(secret, encoding='utf-8'), bytes(message, encoding='utf-8'), digestmod='sha256')
    d = mac.digest()
    return base64.b64encode(d)


def get_header(request_type, endpoint, body, api_key, secret_key, passphrase):
    time = get_time()
    header = dict()
    header['CONTENT-TYPE'] = 'application/json'
    header['OK-ACCESS-KEY'] = api_key
    header['OK-ACCESS-SIGN'] = signature(time, request_type, endpoint, body, secret_key)
    header['OK-ACCESS-TIMESTAMP'] = str(time)
    header['OK-ACCESS-PASSPHRASE'] = passphrase
    return header


def get(endpoint, root_url, api_key, secret_key, passphrase, body=''):
    url = root_url + endpoint
    header = get_header('GET', endpoint, body, api_key, secret_key, passphrase)
    return requests.get(url, headers=header)
