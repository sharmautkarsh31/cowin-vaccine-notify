import datetime

import pytz as pytz

from config import MIN_AGE_LIMIT, SEARCH_BY, PINCODE, DISTRICT_ID

location = PINCODE if SEARCH_BY == 'PINCODE' else DISTRICT_ID

def filter(data):
    data = data.get('centers', [])
    print("Found details of %s centers at %s:%s"% ( str(len(data)), SEARCH_BY, location))
    res = []
    for center_data in data:
        session_data = center_data.get('sessions', [])
        center_details = {
            "center_id": center_data.get('center_id'),
            "name": center_data.get('name'),
            "address": center_data.get('address'),
            "block_name": center_data.get('block_name'),
            "pincode": center_data.get("pincode"),
            "district_name": center_data.get("district_name"),
            "fee_type": center_data.get("fee_type")
        }
        for session in session_data:
            if session.get('min_age_limit', 1000) <= MIN_AGE_LIMIT and session.get('available_capacity', 0)>0:
                print(datetime.datetime.now(tz=pytz.timezone('Asia/Kolkata')).strftime('%H:%M:%S %Y-%m-%d'),
                      "FOUND MATCHING CENTER")
                print("center_id: ", center_details['center_id'],
                      "\nname: ", center_details['name'],
                      '\nblock_name: ', center_details['block_name'],
                      '\npincode: ', center_details['pincode'],
                      '\naddress: ', center_details['address'],
                      '\ndistrict_name: ', center_details['district_name'],
                      '\nfee_type: ', center_details['fee_type'],
                      '\n\n'
                      )
                res.append({**center_details, **session})

    return res