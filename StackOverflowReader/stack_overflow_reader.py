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

count = 1
links = []

print(Fore.GREEN + "\nHere are the results sorted by relevance\n\n")

for i in range(0, (10 if (10 < len(divs)) else len(divs))):
    question = divs[i].a.text.strip()
    if question[0] == "Q":
        #excerpt = divs[i].find("div", {"class" : "excerpt"}).text.strip()
        # FIND LINK
        link = "https://stackoverflow.com" + (divs[i].find("a"))['href'].strip()
        links.append(link)

        # FIND VOTE COUNT
        votes = divs[i].find("span", {"class" : "vote-count-post"}).text.strip()
        votes_text = "vote" if votes == "1" else "votes"
        if int(votes) < 2:
            votes = Fore.RED + votes
        else:
            votes = Fore.GREEN + votes

        # FIND ANSWER COUNT
        try:
            answers = divs[i].find("div", {"class" : "status answered-accepted"}).text.strip()
        except:
            answers = divs[i].find("div", {"class" : "status answered"}).text.strip()
        answers = ''.join(re.findall(r'\d+', answers))
        answers_text = "answer" if answers == "1" else "answers"

        if int(answers) < 1:
            answers = Fore.RED + answers
        else:
            answers = Fore.GREEN + answers

        print(Fore.YELLOW + "Q " + str(count) + ") " + question[3:])
        print("\t", votes, votes_text + ".", answers, answers_text + ".\n")
        count += 1
