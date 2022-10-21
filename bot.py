import requests
from lxml.html import fromstring

with open('username.txt', 'r', encoding='UTF-8') as f:
    for line in f:
        username = line.strip('\n')
        r = requests.get(f"https://www.instagram.com/{username}/")
        tree = fromstring(r.content)
        result = tree.findtext('.//title')
        if "Instagram photos and videos" in result:
            print("Taken "+username)
        else: 
            print("Not Taken "+username)