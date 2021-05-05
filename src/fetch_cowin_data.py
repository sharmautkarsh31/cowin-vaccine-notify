import requests
import urllib.parse
import traceback
from datetime import datetime
from constants import *


def get_date():
    dt = datetime.now()
    return  dt.strftime("%d-%m-%Y")

def get_url(district_code):
    url = urllib.parse.urljoin(BASE_URL, DISTRICT_SEARCH_URL.format(district_code, get_date()))
    return url

def fetch_data(district_code):
    headers = {'Accept': 'application/json',
     'Content-Type': 'application/json',
     'authority': 'cdn-api.co-vin.in'}
    url = get_url(district_code)

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


