import requests

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
