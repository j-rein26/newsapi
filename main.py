import requests
from send_email import send_email

topic = "tesla"

api_key = "f7b82d9c60fe4de39a1276f6da8356da"
url = "https://newsapi.org/v2/everything?" \
    f"q={topic}&" \
    "sortBy=publishedAt" \
    "&apiKey=f7b82d9c60fe4de39a1276f6da8356da&" \
    "language=en"


# make a request
request = requests.get(url)

#Get a dictionary
content = request.json()


# Access the articles with descriptions
body = "Subject: Today's News" + "\n"

for article in content["articles"][0:20]:
    if article["title"] is not None:
        body = body + article["title"] + "\n" \
        + article["description"] + "\n" \
        + article["url"] + 2*"\n"

body = body.encode("utf-8")
send_email(body)

    
    

