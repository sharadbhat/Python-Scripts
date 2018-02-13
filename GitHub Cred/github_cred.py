import requests
import json
import sys

username = input("Enter username: ")

url = "https://api.github.com/users/{}/repos".format(username)

r = requests.get(url=url)
j = json.loads(r.text)

if len(j) == 0:
    print("\nInavlid username")
    sys.exit(0)

total_starred = 0
total_forked = 0

count = 0

if "message" in j:
    if j["message"] == "Not Found":
        print("\nNo repositories found.")
        sys.exit(0)

for i in j:
    count += 1
    print("")
    print("Repository number", count)
    print("Repository name -", i["name"])
    print("Repository description -", i["description"])
    print("Stargazers -", i["stargazers_count"])
    total_starred += i["stargazers_count"]
    print("Forks -", i["forks_count"])
    total_forked += i["forks_count"]

url = "https://api.github.com/users/{}".format(username)

r = requests.get(url=url)
j = json.loads(r.text)

print("\n\nSummary")
print("Name -", j["name"])
print("Username -", username)
print("Bio -", j["bio"])
print("Total number of public repositories -", j["public_repos"])
print("Total number of public gists -", j["public_gists"])
print("Total number of followers -", j["followers"])
print("Total number of stargazers -", total_starred)
print("Total number of forks -", total_forked)
