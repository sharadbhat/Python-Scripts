import requests
import argparse
from requests.utils import quote

parser = argparse.ArgumentParser(description='Get answers from Stack Overflow')
parser.add_argument("-q", "--query", help="Enter question to search SO")
parser.add_argument("-t", "--tag", help="Enter question tag")
args = parser.parse_args()

query = args.query
tag = args.tag


url = "http://stackoverflow.com/search?q=" + quote(query)
