import requests

api_key = "f7b82d9c60fe4de39a1276f6da8356da"
url = "https://newsapi.org/v2/everything?q=tesla&" \
    "from=2024-09-17&sortBy=publishedAt&apiKey=" \
        "f7b82d9c60fe4de39a1276f6da8356da"

# make a request
request = requests.get(url)

#Get a dictionary
content = request.json()

# Access the articles with descriptions
for article in content["articles"]:
    print(article["title"])
    print(article["description"])

    
