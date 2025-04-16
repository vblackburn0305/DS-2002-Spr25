import os
import json
import requests

GHUSER = os.getenv('GITHUB_USER')
print(os.getenv)
url = f"https://api.github.com/users/{GHUSER}/events"
r = json.loads(requests.get(url).text)

