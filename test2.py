import sqlite3

from sqlite3.dbapi2 import Connection
conn = sqlite3.connect('biosprof.db') # DATABA BASE 
# original db access at d:/csharpDevelopment/mysql_carla/bioprofDB.accdb

cursor = conn.cursor()

row = cursor.execute("SELECT prof_id, firstName, lastName, credentials, phoneNumber, photoURL FROM biosprof WHERE prof_id = 1")

for result in row:
   print(result)

firstN = result[1]
print(firstN)
print (result[2])
"""
row = cursor.execute("SELECT prof_id, firstName, lastName, credentials, phoneNumber, photoURL FROM biosprof ORDER by firstName")
size = 15
primary_key = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]  # list of the primary key order by first name
index = 0
for i in row:
    primary_key[index] = i
    print(primary_key[index])
    if index < size:
        index = index + 1
    print('\n')

#print(primary_key[0][0])
i = 0
for x in primary_key:
    print(primary_key[i][0])
    if i < size:
        i = i + 1
"""