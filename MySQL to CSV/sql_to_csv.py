import csv
import pymysql

host = "HOST_NAME" #localhost
user = "MySQL_USERNAME" # root
password = "MySQL_PASSWORD"
database_name = "DATABASE_NAME"

db = pymysql.connect(host=host, user=user, passwd=password, db=database_name)
cur = db.cursor()

cur.execute("SHOW TABLES")

for row_1 in cur.fetchall():
    table_name = row_1[0]
    csv_file = "{}.csv".format(table_name)
    csv_file_write = open(csv_file, "wt", encoding="utf-8", newline='')
    table_writer = csv.writer(csv_file_write)
    cur.execute("SELECT * FROM {}".format(table_name))
    for row_2 in cur.fetchall():
        table_writer.writerow(row_2)
