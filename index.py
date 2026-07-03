import json
import requests
from google.oauth2 import service_account
from google.auth.transport.requests import Request

SCOPES = ["https://www.googleapis.com/auth/indexing"]

credentials = service_account.Credentials.from_service_account_file(
    "credentials.json",
    scopes=SCOPES,
)

credentials.refresh(Request())

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {credentials.token}",
}

with open("urls.txt", "r", encoding="utf-8") as file:
    urls = [line.strip() for line in file if line.strip()]

for url in urls:
    payload = {
        "url": url,
        "type": "URL_UPDATED"
    }

    response = requests.post(
        "https://indexing.googleapis.com/v3/urlNotifications:publish",
        headers=headers,
        data=json.dumps(payload)
    )

    print("=" * 60)
    print("URL:", url)
    print("Status:", response.status_code)
    print(response.text)
