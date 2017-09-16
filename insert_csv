
#### insert csv file into MSSQL SERVER 


import csv
import pymssql


conn = pymssql.connect(server="",
                       user="",
                       password="",
                       database="")
cur = conn.cursor()


#create table

cur.execute("create table mat_2002_new(\
                        코드 varchar(MAX),\
                        적용일자 varchar(MAX),\
                        품명 varchar(MAX), \
                        규격 varchar(MAX),\
                        단위 varchar(MAX),\
                        상한금액 varchar(MAX),\
                        제조회사 varchar(MAX),\
                        재질 varchar(MAX),\
                        수입업소 varchar(MAX))"
            )
print("DB table created!")

#inserting file

with open('C:\치료재료대화일.CSV', 'r') as csvfile:
    #skip the first row
    next(csvfile)
    readCSV = csv.reader(csvfile)
    for row in readCSV:
        query = "INSERT INTO mat_2002_new values (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        cur.execute(query, tuple(row))
    cur.close()
conn.commit()
conn.close()

print("data inserting is finished!")


