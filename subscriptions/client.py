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

import httpx
import asyncio

API_KEY = "YOUR_ACCESS_TOKEN"
API_URL = "http://localhost:8000/api/protected/"

async def call_api():
    async with httpx.AsyncClient() as client:
        response = await client.get(API_URL, headers={"Authorization": f"Bearer {API_KEY}"})
        if response.status_code == 200:
            print("✅ Success:", response.json())
        else:
            print("❌ Errore:", response.status_code, response.text)

asyncio.run(call_api())
