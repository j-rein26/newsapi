import requests
from send_email import send_email


api_key = "f7b82d9c60fe4de39a1276f6da8356da"
url = "https://newsapi.org/v2/top-headlines/?country=us" \
"&apiKey=f7b82d9c60fe4de39a1276f6da8356da"


request = requests.get(url)
content = request.json()


body = "Subject: Today's Headlines" + "\n"
for article in content["articles"][0:20]:
    
    body = body + article["author"] + "\n" \
        + article["title"] + "\n" \
        + article["url"]

body = body.encode("utf-8")
send_email(message=body)

