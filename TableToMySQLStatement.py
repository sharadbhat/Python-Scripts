import csv
import sys
import os.path

file_name = ""

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

    csvFile = open(file_name, "rt", encoding="utf-8")
    csvReader = csv.reader(csvFile)
    csvFile.seek(0)

    MySQL_statement = "INSERT INTO {} VALUES".format(table_name)
    for row in csvReader:
        MySQL_statement += "("
        for item in row:
            if item.isnumeric():
                MySQL_statement += str(item) + ", "
            else:
                item.strip()
                MySQL_statement += "\"{}\", ".format(item)

        MySQL_statement = MySQL_statement[:-2] # To remove extra ", "
        MySQL_statement += "),"

    MySQL_statement = MySQL_statement[:-1] # To remove extra ","
    MySQL_statement += ";"
    print(MySQL_statement)
