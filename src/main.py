import os
import time
from config import SEARCH_BY, PINCODE
from fetch_cowin_data import fetch_data
from filter_data import filter
from playsound import playsound
from config import DISTRICT_ID
from src.constants import SLEEP_TIME


def process(search_code):
    data = fetch_data(search_code)
    matched_sessions = filter(data)
    if matched_sessions:
        playsound('../Rooster.mp3')
    else:
        print("No Match found")

def main():
    search_by = os.environ.get('SEARCH_BY', SEARCH_BY)
    if search_by != 'PINCODE':
        search_code = os.environ.get('DISTRICT_CODE', DISTRICT_ID)
    else:
        search_code = os.environ.get('PINCODE', PINCODE)
    while True:
        print("Starting Process")
        process(search_code)
        print("Sleeping for {} seconds".format(SLEEP_TIME))
        time.sleep(SLEEP_TIME)


if __name__=="__main__":
    main()