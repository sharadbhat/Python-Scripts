import requests
import bs4

url = "https://c.xkcd.com/random/comic/"

r = requests.get(url)
soup = bs4.BeautifulSoup(r.text, 'html.parser')
count = 0
for img in soup.find_all('img'):
    image_url = "http:" + str(img.get('src'))
    image_title = img.get('title')
    if count == 1:
        break
    count = 1

print(image_url)
print(image_title)
