BASE_URL = "https://www.cowin.gov.in"
DISTRICT_SEARCH_URL = "/api/v2/appointment/sessions/public/calendarByDistrict?district_id={}&date={}"
PINCODE_SEARCH_URL = "/api/v2/appointment/sessions/public/calendarByPin?pincode={}&date={}"
SLEEP_TIME = 10 # in seconds
TIMEZONE = 'Asia/Kolkata'

DOSE_TYPE_MAP = {
    "FIRST": "available_capacity_dose1",
    "SECOND": "available_capacity_dose2"
}

VACCINE_MAP = {
    '0' : '',
    '1' : 'COVAXIN',
    '2' : 'COVISHIELD',
    '3' : 'SPUTNIK'
}

BULK_NOTIFY_MAP = {
    "YES": 29,
    "NO": 0
}