import requests
import argparse
from requests.utils import quote
from bs4 import BeautifulSoup

parser = argparse.ArgumentParser(description='Get answers from Stack Overflow')
parser.add_argument("-q", "--query", help="Enter question to search SO")
parser.add_argument("-t", "--tag", help="Enter question tag")
args = parser.parse_args()

query = args.query
tag = args.tag


url = "http://stackoverflow.com/search?q=" + quote(query)

r = requests.get(url=url)

soup = BeautifulSoup(r.text, "lxml")

divs = soup.findAll("div", { "class" : "question-summary search-result"})

for i in range(0, (10 if (10 < len(divs)) else len(divs))):
    print(divs[i].a.text.strip())
