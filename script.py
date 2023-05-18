import sqlite3
from sqlite3.dbapi2 import Connection
conn = sqlite3.connect('biosprof.db') # DATABA BASE 
# original db access at d:/csharpDevelopment/mysql_carla/bioprofDB.accdb

cursor = conn.cursor()

porf_Key = 15
firstN = "Scott"
lastN= "Rush"

cred = "M.S., LPCC"



photoNumber = "(937) 802-0727"
               
urlPhoto = "http://www.procounselgroup.com/wp-content/uploads/2021/01/scott_rush.jpg"
 #  table 1 biosprof

#  to use variables need to use the ?? like this:

cursor.execute( "INSERT INTO biosprof VALUES (?,?,?,?,?,?)",
                  (porf_Key,firstN ,lastN,cred,photoNumber, urlPhoto) )

# Biography

bioDes = "Scott is a licensed professional clinical counselor with three years experience in the mental health field.\n"

bioDes2 = "He has a background of working with children, adolescents, adults, families, and group therapy.\n"
 
bioDes3 = "Scott’s approach to counseling is to empower clients to focus on individual strengths, values, and on becoming an expert of one’s own life.\n"

bioDes4 = "He utilizes an eclectic approach to therapy to meet the client’s individual needs. He utilizes Cognitive Behavioral Therapy., Solution Focused Therapy, Client Centered Therapy, and Trauma Focused-Cognitive Behavioral Therapy.\n"

bioDes5 = "He provides empathy, self-acceptance, and allows clients to experience a judgement free and confidential space to express one’s thoughts, feelings, and emotions.\n"

bioDes6 = "Scott is passionate about working with clients who have anxiety and depression disorders. He is interested in helping those that are struggling with life’s challenges.\n"

bioDes7 = "He is an empathetic listener who will do everything he can to help a client feel heard and that their emotions are validated.\n"

bioDes = bioDes + bioDes2 + bioDes3 + bioDes4 + bioDes5 + bioDes6 + bioDes7

educ =  "Scott graduated from the University of Akron in 2014 with a B.A. in psychology and a minor in sociology.\n"

educ1 = "He continued his studies at Wright State University and graduated in 2017 with Master of Science in Clinical Mental Health Counseling.\n"

educ2 = ""
educ3 = ""
#educ = educ + educ1 + educ2 + educ3
#educ = "*"
#  License

#lic = "*"

#lic1 = "– State of Ohio Licensed Independent Chemical Dependency Counselor\n"
#lic2 = "– State of Ohio Certified High Performance Coach\n"
#lic3 = "– High Performance Institute\n"
#lic = lic + lic1 + lic2 + lic3
# lic = lic + lic1
#"lic = "Licensed Counselor by the State of Ohio\n"
lic = "Licensed professional clinical counselor\n"
cursor.execute("INSERT INTO bios VALUES (?,?,?,?)",(porf_Key,bioDes,educ,lic))
conn.commit()               

