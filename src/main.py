import os
import time
from config import SLEEP_TIME
from fetch_cowin_data import fetch_data
from filter_data import filter
from data_to_csv import write_data
# from send_email import send_email


def process(district_code):
    data = fetch_data(district_code)
    matched_sessions = filter(data)
    if matched_sessions:
        pass
#         filename = '/tmp/sessions.csv'
#         write_data(filename, matched_sessions)
#         send_email(filename)
#         send_data(matched_sessions)
    else:
        print("No Match found")


def main():
    district_code = os.environ.get('DISTRICT_CODE', '637')
    while True:
        print("Starting Process")
        process(district_code)
        print("Sleeping for {} seconds".format(SLEEP_TIME))
        time.sleep(SLEEP_TIME)
#     process(district_code)


if __name__=="__main__":
    main()