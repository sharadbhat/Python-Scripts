import requests
import argparse
from requests.utils import quote
from bs4 import BeautifulSoup
import re
from colorama import init, Fore

init(autoreset=True)

parser = argparse.ArgumentParser(description='Get answers from Stack Overflow')
parser.add_argument("-q", "--query", help="Enter question to search SO")
parser.add_argument("-t", "--tag", help="Enter question tag")
args = parser.parse_args()

query = args.query
tag = args.tag

url = "http://stackoverflow.com/search?q=" + quote(query)

r = requests.get(url=url)

soup = BeautifulSoup(r.text, "lxml")

divs = soup.findAll("div", {"class" : "question-summary search-result"})

for i in range(0,15):# (10 if (10 < len(divs)) else len(divs))):
    question = divs[i].a.text.strip()
    if question[0] == "Q":
        excerpt = divs[i].find("div", {"class" : "excerpt"}).text.strip()
        votes = divs[i].find("span", {"class" : "vote-count-post"}).text.strip()
        try:
            answers = divs[i].find("div", {"class" : "status answered-accepted"}).text.strip()
        except:
            answers = divs[i].find("div", {"class" : "status answered"}).text.strip()
        answers = ''.join(re.findall(r'\d+', answers))
        print(Fore.YELLOW + question)
        print(excerpt)
        votes_text = "vote" if votes == "1" else "votes"
        answers_text = "answer" if answers == "1" else "answers"
        print(votes, votes_text + ".", answers, answers_text + ".")
