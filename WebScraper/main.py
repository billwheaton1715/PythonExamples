import requests
from bs4 import BeautifulSoup as bs

github_user = input("enter github username: ")

url = f"https://github.com/{github_user}"
req = requests.get(url)
soup = bs(req.content, "html.parser")
profile_image_url = soup.find("img", class_="avatar")["src"]
print (profile_image_url)


