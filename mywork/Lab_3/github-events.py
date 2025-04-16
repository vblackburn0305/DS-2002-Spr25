#!/Library/Frameworks/Python.framework/Versions/3.10/bin/python3

import os
import json
import requests

GHUSER = os.getenv('GITHUB_USER')
url = f"https://api.github.com/users/{GHUSER}/events"
r = json.loads(requests.get(url).text)

for x in r[:5]:
  event = x['type'] + ' :: ' + x['repo']['name']
  print(event)