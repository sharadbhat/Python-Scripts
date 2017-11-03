import csv
import sys
import os.path
from dateutil.parser import parse

file_name = ""

def is_date(string):
    try:
        parse(string)
        return True
    except ValueError:
        return False


try:
    file_name = sys.argv[1]
except:
    print("No filename provided")

if os.path.isfile(file_name) == False:
    print("No such file present in current directory")
else:
    table_name = ""
    try:
        table_name = sys.argv[2]
    except:
        print("No table name provided")

    csv_file = open(file_name, "rt", encoding="utf-8")
    csv_reader = csv.reader(csv_file)
    csv_file.seek(0)

    MySQL_statement = "INSERT INTO {} VALUES".format(table_name)
    for row in csv_reader:
        MySQL_statement += "("
        for item in row:
            if item.isnumeric():
                MySQL_statement += str(item) + ", "
            elif is_date(item) == True:
                date = parse(item)
                date_string = "{0:0=4d}".format(date.year) + "/" + "{0:0=2d}".format(date.month) + "/" + "{0:0=2d}".format(date.day)
                MySQL_statement += "\'{}\', ".format(date_string)
            else:
                item.strip()
                MySQL_statement += "\"{}\", ".format(item)

        MySQL_statement = MySQL_statement[:-2] # To remove extra ", "
        MySQL_statement += "),"

    MySQL_statement = MySQL_statement[:-1] # To remove extra ","
    MySQL_statement += ";"
    print(MySQL_statement)
