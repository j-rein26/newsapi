import requests
from send_email import send_email

api_key = "f7b82d9c60fe4de39a1276f6da8356da"
url = "https://newsapi.org/v2/everything?q=tesla&" \
    "from=2024-09-17&sortBy=publishedAt&apiKey=" \
        "f7b82d9c60fe4de39a1276f6da8356da"


# make a request
request = requests.get(url)

#Get a dictionary
content = request.json()

# Access the articles with descriptions
body = ""
for article in content["articles"]:
    if article["title"] is not None:
        body = body + article["title"] + "\n" + str(article["description"]) + 2*"\n"

body = body.encode("utf-8")
send_email(message=body)

    
    

