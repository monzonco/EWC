import sqlite3
from contextlib import closing, nullcontext
import sys

from sqlite3.dbapi2 import Connection
conn = sqlite3.connect('EWC_db.db')   
cursor = conn.cursor()

lineOne = "<a name=\"top\"></a>" 
lineTwo = "<h3>Note: For Other Phone and Emergency Contact Listing <a href=\"#emergency\">Click here</a></h3>" 
lineThree = "<a name=\"emergency\"></a>" 
lineFive = "<a href=\"#top\">Top</a>" 
divRounded = "<div class= \"redonda\">"
table = "<table><tbody>" 
lineTableLabel = "<tr><th>Last Name</th><th>First Name</th><th>Unit</th><th>Address Line</th><th>Telephone</th></tr>"
endofTable = "</tbody></table>"
newRow = "<tr>"
endOfRow = "</tr>"
column = "<td>"
endOfColumn = "</td>"
lineStreetTable = "<table class=\"streetTable\"><tbody>"
streetTableCaption = "<caption> Residents List by Court Address</caption>"
lineStreetTableLabel = "<tr><th>Resident</th><th>Unit</th><th>Address Line</th><th>Telephone</th></tr>"
lineStreetEmergencyLabel = "<tr><th>Resident</th><th>Unit</th><th>Address Line</th><th>Other Phone</th><th>Emergency Contact</th></tr>"

addressLine = {
    1: "Ashworth Ct.",
    2: "Beckett Ct.",
    3: "Greyfield Ct.",
    4: "Muirfield Ct.",
    5: "Trafalgar Ct.",
    6: "Weatherfield Ct.",
    7: "Wembley Cr." 
} 
clubhouse = {
    "lastName" :"Clubhouse",
    "unit" : "6980",
    "address" : "Wembley Ct.",
    "phone"  : "937-438-1253"
}
def getLandlord(lid): 
    conn = sqlite3.connect('EWC_db.db') 
     
    sqllord = """SELECT id, lord_name, address, city, state, zip_code, unit_symbol, phone FROM land_lords where id = ?"""    
    
    with closing(conn.cursor()) as c:
        c.execute(sqllord,(lid,))
        res = c.fetchall()       
    for value in res:
                name = value[1]                
                addrs = value[2]
                town = value[3]
                stat = value[4]                
                zip   = value[5]                
                un  = value[6]                
                phon = value[7]                
                
    
    line2 = column + name + endOfColumn +column +un+ endOfColumn + column + addrs+ "<br>" +town +" " +  stat+" " + zip +endOfColumn +column + phon +endOfColumn         
    return line2
def writeStreetDirectory():            
            fileName = "c:\\temp\\streetDir_newP.html"  
            streethtmlFileOut = open(fileName,"w")  
            streethtmlFileOut.write(lineOne+"\n")            
            streethtmlFileOut.write(divRounded+ "\n") 
            
            streethtmlFileOut.write(table+"\n")  
            streethtmlFileOut.write(lineStreetTable+"\n")
            streethtmlFileOut.write(streetTableCaption+ "\n")
            streethtmlFileOut.write(lineStreetTableLabel+ "\n")
            conn = sqlite3.connect('EWC_db.db')     
            cursor = conn.cursor()
            try:
                sql = "SELECT id,first_name, last_name, land_lord_id, unit_number, court_id, phone FROM resident WHERE id < 133 order by court_id"
                with closing(conn.cursor()) as c:
                    c.execute(sql)                             
                    result  = c.fetchall()    
                    for value in result:                                    
                        line = newRow
                        streethtmlFileOut.write(line) 
                        firstN = value[1]
                        lastN = value[2]
                        tenant = value[3]
                        unitN = value[4]
                        courtId = value[5]
                        phone = value[6]
                        if phone is None:
                            phone = ""  
                        line1 = column + firstN + " " +lastN + endOfColumn + column + str(unitN) + endOfColumn + column + addressLine[courtId] + endOfColumn + column + phone + endOfColumn 
                      
                        streethtmlFileOut.write(line1) 
                        line = endOfRow  
                        streethtmlFileOut.write(line+"\n" ) 

                        if tenant > 0:                       
                            #landLordRelated = findLandlord(tenant)  
                            line = newRow 
                            streethtmlFileOut.write(line) 
                            #line = column + landLordRelated.lastName + endOfColumn + column + landLordRelated.firstName + endOfColumn + column + " " + endOfColumn + column + landLordRelated.addressLine + endOfColumn + column + landLordRelated.phone + endOfColumn + column + landLordRelated.email + endOfColumn  
                            line = getLandlord(tenant)
                            streethtmlFileOut.write(line) 
                            line = endOfRow
                            streethtmlFileOut.write(line) 
                       
                    
               
                line = newRow  
                streethtmlFileOut.write(line) 
                line = column + clubhouse["lastName"] + endOfColumn + column + clubhouse["unit"]+ endOfColumn + column + clubhouse['address'] + endOfColumn + column + clubhouse["phone"] + endOfColumn + column + endOfColumn  
                streethtmlFileOut.write(line) 
                line = endOfRow 
                streethtmlFileOut.write(line + "\n")                
                
                                
            except :           
                print("at writestreetDirectory,Exception : " ) 
                cursor.close() 
            streethtmlFileOut.write ("\n")
            streethtmlFileOut.write(endofTable)   #writestreetEmergencyDirectory()  
            streethtmlFileOut.write("</div>\n")  
            streethtmlFileOut.write (lineFive)

            streethtmlFileOut.close()               
writeStreetDirectory()
           
    
