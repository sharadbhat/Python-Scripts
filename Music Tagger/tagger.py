import requests

client_id = "e8e679012a864e66a272d18bfd4f475c"
client_secret = ""
with open("key.txt", "r") as f:
    client_secret = f.readline().strip()

print(client_secret)
