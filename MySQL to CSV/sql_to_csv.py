import csv
import pymysql
import argparse
import os

parser = argparse.ArgumentParser(description='Convert SQL database to CSV files.')
parser.add_argument("-ht", "--host", help="Enter MySQL host name")
parser.add_argument("-u", "--user", help="Enter MySQL username")
parser.add_argument("-p", "--password", help="Enter MySQL password")
parser.add_argument("-db", "--database", help="Enter database name")
args = parser.parse_args()

host = args.host # localhost
user = args.user # root
password = args.password
database_name = args.database

db = pymysql.connect(host=host, user=user, passwd=password, db=database_name)
cur = db.cursor()

cur.execute("SHOW TABLES")

os.mkdir("./{}".format(database_name))
os.chdir("./{}".format(database_name))

for row_1 in cur.fetchall():
    table_name = row_1[0]
    csv_file = "{}.csv".format(table_name)
    with open(csv_file, "wt", encoding="utf-8", newline='') as csv_file_write:
        table_writer = csv.writer(csv_file_write)
        cur.execute("DESC {}".format(table_name))
        column_names = []
        for column in cur.fetchall():
            column_names.append(column[0])
        columns = tuple(column_names)
        table_writer.writerow(columns)
        cur.execute("SELECT * FROM {}".format(table_name))
        for row_2 in cur.fetchall():
            table_writer.writerow(row_2)
