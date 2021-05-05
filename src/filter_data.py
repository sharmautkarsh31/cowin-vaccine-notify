from config import MIN_AGE_LIMIT

res = []

def filter(data):
    data = data.get('centers', [])
    print("Found details of {} centers".format(len(data)))

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
                print("FOUND MATCHING CENTER")
                print(session, center_details)
                res.append({**center_details, **session})

    return res