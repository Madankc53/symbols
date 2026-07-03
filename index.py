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

SITEMAP = "https://symbols.thenepal.io/sitemap.xml"

xml = requests.get(SITEMAP).text
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
