"""
- Sharad Bhat
- 11th December, 2017
"""

import requests
import os
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, APIC, TIT2, TPE2, TALB

Tk().withdraw()

filename = askopenfilename()
track = input("Enter track name: ")
artist = input("Enter artist name: ")

invalid_characters = ['/', '\\', ':', '?', '*', '|', '<', '>', '"']

if not os.path.isfile(filename):
    print("INVALID FILE PATH")
    exit()

if filename[-3:] != 'mp3':
    print("Supports only mp3 files.")
    exit()

client_id = "e8e679012a864e66a272d18bfd4f475c"
client_secret = ""
with open("key.txt", "r") as f:
    client_secret = f.readline().strip()

body = {"grant_type" : "client_credentials",
        "client_id" : client_id,
        "client_secret" : client_secret}
r = requests.post(url="https://accounts.spotify.com/api/token", data=body)
r = r.json()

token = r["access_token"]

print("Downloading track information")

head = {"Authorization" : "Bearer " + token}
url = "https://api.spotify.com/v1/search?q=track:{}&artist:{}&type=track".format(track, artist)

r = requests.get(url=url, headers = head)
r = r.json()

artist_name = []
image_url = []
album_name = []
track_name = []

for i in r["tracks"]["items"]:
    artist_name.append(i["artists"][0]["name"])
    image_url.append(i["album"]["images"][0]["url"])
    album_name.append(i["album"]["name"])
    track_name.append(i["name"])

offset = 0
flag = False
while True:
    for i in range(offset, (offset + 5) if (offset + 5) < len(artist_name) else len(artist_name)):
        print(str(i + 1) + ".")
        print("Artist: " + artist_name[i])
        print("Track: " + track_name[i])
        print("Album: " + album_name[i])
        print("")

    if offset + 5 < len(artist_name):
        print("Press \"N\" for next 5 tracks")
        print("Or press \"Q\" to quit")
    else:
        flag = True
        print("No more tracks available.")
        print("Press \"Q\" to quit")
    choice = input("Or select a track: ").lower()
    if choice == "n":
        if flag == True:
            offset = len(artist_name)
            print("\nNo more tracks available.")
        else:
            offset += 5 if 5 < (len(artist_name) - offset) else (len(artist_name) - offset)
    elif choice == "q":
        exit()
    else:
        choice = int(choice)
        if choice < 0 or choice > ((offset + 5) if (offset + 5) < len(artist_name) else len(artist_name)):
            print("Choice invalid.")
            exit()
        choice -= 1
        break



print("Downloading album art")

imagedata = requests.get(image_url[choice]).content

id3 = ID3(filename)
id3.add(APIC(3, 'image/jpeg', 3, 'Front cover', imagedata))
id3.add(TIT2(encoding=3, text=track_name[choice]))
id3.add(TALB(encoding=3, text=album_name[choice]))
id3.add(TPE2(encoding=3, text=artist_name[choice]))
id3.save(v2_version=3)

for i in invalid_characters:
    if i in artist_name[choice]:
        artist_name[choice] = artist_name[choice].replace(i, "")
    if i in track_name[choice]:
        track_name[choice] = track_name[choice].replace(i, "")


# To rename the filename. Currently only for Windows.
file2 = filename.replace(os.path.basename(filename), artist_name[choice] + " - " + track_name[choice] + ".mp3")

print("Renaming filename to \"{} - {}.mp3\"".format(artist_name[choice], track_name[choice]))

os.rename(filename, file2)
