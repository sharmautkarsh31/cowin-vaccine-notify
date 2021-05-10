import os
import time

import pytz
import requests
import urllib.parse
import traceback
import datetime
from constants import BASE_URL, DISTRICT_SEARCH_URL, PINCODE_SEARCH_URL, TIMEZONE
from config import SEARCH_BY, DATE


def get_date():
    dt = datetime.datetime.now(tz=pytz.timezone(TIMEZONE))
    today = dt.strftime("%d-%m-%Y")
    today_timestamp = dt.timestamp()
    entered_date_timestamp = time.mktime(datetime.datetime.strptime(DATE,
                                             "%d-%m-%Y").timetuple())

    if today_timestamp < entered_date_timestamp:
        return DATE
    else:
        return today

def get_url(search_code):
    search_by = os.environ.get('SEARCH_BY', SEARCH_BY)
    if search_by != 'PINCODE':
        url = urllib.parse.urljoin(BASE_URL, DISTRICT_SEARCH_URL.format(search_code, get_date()))
    else:
        url = urllib.parse.urljoin(BASE_URL, PINCODE_SEARCH_URL.format(search_code, get_date()))
    return url

def fetch_data(search_code):
    headers = {'Accept': 'application/json',
     'Content-Type': 'application/json',
     'authority': 'cdn-api.co-vin.in'}
    url = get_url(search_code)

    val = {}

    try:
        data=requests.get(url, headers=headers)
        if data.status_code != 200:
            print("Not able to fetch data received status_code {}".format(data.status_code))
            print("Error - ", data.content)
        else:
            val = data.json()
    except Exception as e:
        print("Error fetching data")
        print(e)
        print(traceback.print_stack())

    return val


