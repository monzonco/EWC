import sqlite3
from contextlib import closing, nullcontext
import sys
import datetime
import csv as xw
#import XlsxWriter as xw

#from xlsxwriter import Workbook
from sqlite3.dbapi2 import Connection
conn = sqlite3.connect('EWC_db.db')
courts = {1:"Ashworth Ct.", 2:"Beckett Ct.",3:"Greyfield Ct.",4:"Muirfield",5:"Trafalgar Ct.",6:"Weatherfield Ct.",7:"Wembley Cr." }   

def get_file_name():
    fecha= datetime.datetime.now()
    tailYear = fecha.year
    tailMonth = fecha.month
    tailDay = fecha.day
    tailSeconds = fecha.second
    str_trail = "_" + str(tailYear) + "_" + str(tailMonth) + "_" + str(tailDay) + "_" + str(tailSeconds) + ".csv"
    fileName = "c:\\temp\\PropertyRevision" + str_trail
    return fileName

def get_land_lord(id ):
    sql = "SELECT * FROM land_lords   WHERE id = ?"
    with closing(conn.cursor()) as c:            
            c.execute(sql,(id,))
            result = c.fetchall()
            for x in result: 
                l_n = x[1]
                addr = x[2]
                ciudad = x[3]
                st = x[4]
                zp = x[5]
                unit_s = x[6]
                ph = x[7]
                other = x[8]
                em = x[9]
                notas = x[10]
            
            resident = unit_s + " "+ l_n
            rent = " "
            unit = " "
            line = [resident, rent,unit,addr,ciudad,st, zp,ph, other,em,notas]
            return line
def write_Excel_file():    
    file_name = get_file_name()
    header =['Resident','Renter', 'Unit', 'Adress','City','State','Zip','Telephone','Other Phone','Email','Emergency','Notes']
    with open(file_name, "w", encoding='UTF8') as f:
        conn = sqlite3.connect('EWC_db.db')   
        writer = xw.writer(f)
        writer.writerow(header)
        sql = "SELECT * FROM resident ORDER BY court_id"
        with closing(conn.cursor()) as c:            
            c.execute(sql)
            result = c.fetchall()
            for x in result:
                firstN = x[1]
                lastN = x[2]
                renter = x[3]
                unitN = x[4]          
                c_id = x[5]
                phon = x[6]
                other = x[7]
                e_mail = x[8]                
                notas = x[9]
                resident = firstN + " " + lastN
                if renter == 0:
                    renter_out = " "
                else:
                    renter_out = "Tenant"
                c_name = courts[c_id]
                line = [resident,renter_out,unitN,c_name, "Centerville", "OH","45459",phon,other,e_mail, notas]
                writer.writerow(line)
                if renter > 0:
                    line = get_land_lord(renter)
                    writer.writerow(line)                    
    conn.commit()
    conn.close()

write_Excel_file()
