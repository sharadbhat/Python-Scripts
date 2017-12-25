import requests
import json
import ctypes

API_KEY = "******"
unsplash_url = "https://api.unsplash.com/photos/random?w=1920&h=1080&client_id={}".format(API_KEY)

r = requests.get(url=unsplash_url, headers = {"Accept-Version" : "v1"})
a = json.loads(r.text)

url = a["urls"]["custom"]

f = open('image.jpg','wb')
f.write(requests.get(url).content)
f.close()

ctypes.windll.user32.SystemParametersInfoW(20, 0, "C:\\Users\\Sharad\\Documents\\GitHub\\Python-Scripts\\Wallpaper Updater\\image.jpg" , 0)
