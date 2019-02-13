# -*- coding: UTF-8 -*-
import os
import datetime
import time
import json
import random
import string

import urllib
import urllib2
import urllib3

key = 'PsJorfW9NYUWRitA'

domain = 'http://admin.seanking.top'
add_url = '/Api/User/add'
list_url = '/Api/MailImap/getListMessage'
msg_url = '/Api/MailImap/getMessage'

server_name = "seanking.top"

filename = "user_account.txt"

def date_string():
    now = datetime.datetime.now()
    return datetime.datetime.strftime(now, "yyyymmddHHMMSS")

def save_file(data, filepath):
    if os.path.exists(filepath):
       os.command("mv %s %s_%s" %(filepath, filepath, date_string()), shell=True)
    f = open(filename, 'w')
    f.writelines(data)
    f.close()

def scrapy(url, params, method='get', headers={}, fmt='json'):

    headers[
            'User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'

    params["key"] = key

    http = urllib3.PoolManager()
    r = http.request(method, url, headers=headers, fields=params)

    result = r.data.decode()

    if fmt == 'json':
        try:
            result = json.loads(result)
            if result.get('message') is not None:
                    print("api message: %s" % result.get('message'))
        except Exception as ex:
                print(r.data, ex)


    return result

def create_user():
    accounts = []
    while len(accounts) < 1:
        username = ''.join(random.sample(string.ascii_letters + string.digits, 6))
        password = ''.join(random.sample(string.ascii_letters + string.digits, 8))
        params = {
            "email": "%s@%s" %(username, server_name),
            "password": password,
            "active": 1
        }
        result = scrapy(add_url, params)
        if result.get('status') == 1:
            id = result.get('data', {}).get('id')
            accounts.append("%s %s %s" %(id, username, password))

    print('finish jobs')


