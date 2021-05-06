import os
import time
from config import SLEEP_TIME
from fetch_cowin_data import fetch_data
from filter_data import filter
from playsound import playsound
from config import DISTRICT_ID

def process(district_code):
    data = fetch_data(district_code)
    matched_sessions = filter(data)
    if matched_sessions:
        playsound('/Users/utkarshsharma/Desktop/CoWin/Rooster.mp3')
    else:
        print("No Match found")

def main():
    district_code = os.environ.get('DISTRICT_CODE', DISTRICT_ID)
    while True:
        print("Starting Process")
        process(district_code)
        print("Sleeping for {} seconds".format(SLEEP_TIME))
        time.sleep(SLEEP_TIME)


if __name__=="__main__":
    main()