import sqlite3
from sqlite3.dbapi2 import Connection
conn = sqlite3.connect('biosprof.db') # DATABA BASE 
# original db access at d:/csharpDevelopment/mysql_carla/bioprofDB.accdb

cursor = conn.cursor()

porf_Key = ""
firstN = ""
lastN= ""
cred = ""
photoNumber = ""               
urlPhoto = ""
 #  table 1 biosprof

#  to use variables need to use the ?? like this:

cursor.execute( "INSERT INTO biosprof VALUES (?,?,?,?,?,?)",
                  (porf_Key,firstN ,lastN,cred,photoNumber, urlPhoto) )

# Biography

bioDesc = ""
educ = ""
#  License
lic = ""

################
cursor.execute("INSERT INTO bios VALUES (?,?,?,?)",(porf_Key,bioDesc,educ,lic))
conn.commit()               

