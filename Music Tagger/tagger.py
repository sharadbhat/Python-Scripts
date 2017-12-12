"""
- Sharad Bhat
- 11th December, 2017
"""

import requests
import argparse
import os
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, APIC, TIT2, TPE1, TALB

parser = argparse.ArgumentParser(description='Add metadata to your music')
parser.add_argument("-f", "--file", help="Enter path to music file", required=True)
parser.add_argument("-t", "--track", help="Enter track name", required=True)
parser.add_argument("-a", "--artist", help="Enter artist name", required=True)
args = parser.parse_args()

file = args.file
track = args.track
artist = args.artist

invalid_characters = ['/', '\\', ':', '?', '*', '|', '<', '>', '"']

if not os.path.isfile(file):
    print("INVALID FILE PATH")
    exit()

if file[-3:] != 'mp3':
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
print(url)
r = requests.get(url=url, headers = head)
print(r.text)
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

for i in range(len(artist_name)):
    print(i + 1)
    print("Artist: " + artist_name[i])
    print("Track: " + track_name[i])
    print("Album: " + album_name[i])
    print("")

choice = int(input("Select a track: ")) - 1

print("Downloading album art")

imagedata = requests.get(image_url[choice]).content

id3 = ID3(file)
id3.add(APIC(3, 'image/jpeg', 3, 'Front cover', imagedata))
id3.add(TIT2(encoding=3, text=track_name[choice]))
id3.add(TALB(encoding=3, text=album_name[choice]))
id3.add(TPE1(encoding=3, text=artist_name[choice]))

id3.save(v2_version=3)

for i in invalid_characters:
    if i in artist_name[choice]:
        artist_name[choice] = artist_name[choice].replace(i, "")
    if i in track_name[choice]:
        track_name[choice] = track_name[choice].replace(i, "")


# To rename the file. Currently only for Windows.
file2 = file.replace(os.path.basename(file), artist_name[choice] + " - " + track_name[choice] + ".mp3")

print("Renaming file to \"{} - {}.mp3\"".format(artist_name[choice], track_name[choice]))

os.rename(file, file2)
