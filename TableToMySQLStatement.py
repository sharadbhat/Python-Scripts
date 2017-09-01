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

    csv_file = open(file_name, "rt", encoding="utf-8")
    csv_reader = csv.reader(csv_file)
    csv_fle.seek(0)

    MySQL_statement = "INSERT INTO {} VALUES".format(table_name)
    line_number = 1
    for row in csv_reader:
        item_number = 1
        if line_number == 1:
            MySQL_statement += "("
            line_number += 1
        else:
            MySQL_statement += ",("
        for item in row:
            if item_number != 1:
                MySQL_statement += ", "
            if item.isnumeric():
                MySQL_statement += item
                item_number += 1
            else:
                MySQL_statement += "\"{}\"".format(item)
                item_number += 1

        MySQL_statement += ")"
    MySQL_statement += ";"
    print(MySQL_statement)
