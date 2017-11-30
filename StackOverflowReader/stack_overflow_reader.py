import requests
import argparse
from requests.utils import quote
from bs4 import BeautifulSoup
import re
from colorama import init, Fore

def print_questions(questions, votes_list, answers_list):
    """
    -   Prints data on to the screen with colours.
    """
    count = 1
    print(Fore.GREEN + "\nHere are the results sorted by relevance\n\n")
    for i in range(0, len(questions)):
        question = questions[i]

        votes = votes_list[i]
        votes_text = "vote" if votes == "1" else "votes"

        # SET COLOUR
        if int(votes) < 2:
            votes = Fore.RED + votes
        else:
            votes = Fore.GREEN + votes

        answers = answers_list[i]
        answers_text = "answer" if answers == "1" else "answers"

        # SET COLOUR
        if int(answers) < 1:
            answers = Fore.RED + answers
        else:
            answers = Fore.GREEN + answers

        print(Fore.YELLOW + "Q " + str(count) + ") " + question[3:])
        print("\t", votes, votes_text + ".", answers, answers_text + ".\n")
        count += 1

    user_choice = int(input("Enter question number to get answers: ")) - 1
    return user_choice

def get_questions_data(soup):
    """
    -   Extracts relevant data from HTML page.
    """
    count = 1
    links = []
    questions = []
    votes_list = []
    answers_list = []
    divs = soup.findAll("div", {"class" : "question-summary search-result"})
    for i in range(0, (10 if (10 < len(divs)) else len(divs))):
        #excerpt = divs[i].find("div", {"class" : "excerpt"}).text.strip()
        question = divs[i].a.text.strip()
        if question[0] == "Q":
            questions.append(question)

            link = "https://stackoverflow.com" + (divs[i].find("a"))['href'].strip()
            links.append(link)

            votes = divs[i].find("span", {"class" : "vote-count-post"}).text.strip()
            votes_list.append(votes)

            try:
                answers = divs[i].find("div", {"class" : "status answered-accepted"}).text.strip()
            except:
                answers = divs[i].find("div", {"class" : "status answered"}).text.strip()
            answers = ''.join(re.findall(r'\d+', answers))
            answers_list.append(answers)

    return questions, links, votes_list, answers_list


if __name__ == '__main__':
    init(autoreset=True) # For colorama

    url = "http://stackoverflow.com/search?q="

    parser = argparse.ArgumentParser(description='Get answers from Stack Overflow')
    parser.add_argument("-q", "--query", help="Enter question to search SO", required=True)
    parser.add_argument("-t", "--tag", help="Enter question tag")
    args = parser.parse_args()

    query = args.query
    tag = args.tag

    if tag:
        url += "[{}]+".format(quote(tag))

    url += quote(query)

    r = requests.get(url=url)
    soup = BeautifulSoup(r.text, "lxml")

    # GET DATA
    questions, links, votes_list, answers_list = get_questions_data(soup)

    # PRINT QUESTIONS
    user_choice = print_questions(questions, votes_list, answers_list)

    print(user_choice)
