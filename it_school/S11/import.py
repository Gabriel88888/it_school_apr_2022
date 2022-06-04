# from datetime import date, datetime
# #data si ora curenta

# now = datetime.now()
# print(now)

import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts/1")

print(response.status_code)

if response.status_code == 200:
    print("Connected")
    print(response.json())
else:
    print("Not connected")