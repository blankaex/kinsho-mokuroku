import bs4, requests

url = input("Album URL: ")
print("Fetching...")

response = requests.get(url)
soup = bs4.BeautifulSoup(response.text, "html.parser")
divs = soup.findAll("div", class_="post-image-container")

print("---\n")

for div in divs:
    print("![](https://i.imgur.com/{}.png)\n".format(div['id']))
