"""import requests

API_KEY = "YOUR_ACCESS_TOKEN"
API_URL = "http://localhost:8000/api/protected/"

headers = {
    "Authorization": f"Bearer {API_KEY}"
}

response = requests.get(API_URL, headers=headers)

if response.status_code == 200:
    print("✅ Success:", response.json())
else:
    print("❌ Errore:", response.status_code, response.text)
"""

from getref.settings import CLIENT_ID, CLIENT_SECRET, DOMAIN
import httpx
import asyncio

#CLIENT_ID = "YOUR_CLIENT_ID"
#CLIENT_SECRET = "YOUR_CLIENT_SECRET"

def get_access_token():
    response = httpx.post(f"{DOMAIN}/o/token/", data={
        "grant_type": "client_credentials",
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET
    })
    return response.json().get("access_token")

API_KEY = get_access_token()
print("🔑 Access Token:", API_KEY)


#API_KEY = "YOUR_ACCESS_TOKEN"
API_URL = f"{DOMAIN}/api/v0/protected/"

async def call_api():
    async with httpx.AsyncClient() as client:
        response = await client.get(API_URL, headers={"Authorization": f"Bearer {API_KEY}"})
        if response.status_code == 200:
            print("✅ Success:", response.json())
        else:
            print("❌ Errore:", response.status_code, response.text)

asyncio.run(call_api())
