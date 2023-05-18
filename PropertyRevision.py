from ctypes import LittleEndianStructure
from os import linesep
import sqlite3
from contextlib import closing, nullcontext
import sys
import datetime

import xlsxwriter as xw

from xlsxwriter import Workbook
from sqlite3.dbapi2 import Connection

conn = sqlite3.connect("d:\\python_work\\EWC_db.db")   
cursor = conn.cursor() 
courts = {1:"Ashworth Ct.", 2:"Beckett Ct.",3:"Greyfield Ct.",4:"Muirfield Ct.",5:"Trafalgar Ct.",6:"Weatherfield Ct.",7:"Wembley Cr." }   

def get_file_name():
    fecha= datetime.datetime.now()
    tailYear = fecha.year
    tailMonth = fecha.month
    tailDay = fecha.day
    tailSeconds = fecha.second
    str_trail = "_" + str(tailYear) + "_" + str(tailMonth) + "_" + str(tailDay) + "_" + str(tailSeconds) + ".xlsx"
    fileName = "c:\\temp\\PropertyRevision" + str_trail
    return fileName

def get_land_lord(id ):
    sql = "SELECT * FROM land_lords   WHERE id = ?"

    coursor = conn.cursor()          
    coursor.execute(sql,(id,)) 
    result = coursor.fetchall()
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
            
    house = unit_s + " "+ l_n
    rent = " "
    unit = " "
    line = [house,addr,ciudad,st, zp,ph, other,em,notas]
    return line

def write_Excel_file():    
    file_name = get_file_name()
    header =['Resident','Renter', 'Unit', 'Address','City','State','Zip','Telephone','Other Phone','Email','Emergency Contact','Notes']
    workbook = Workbook(file_name)
    worksheet = workbook.add_worksheet("Estates at the Willow Creek")
    the_header = workbook.add_format(
        {
            "font" : "Calibri",
            "font_size" : 14,
            "bold" :True
        }
    )
    the_body = workbook.add_format(
        {
            "font" : "Calibri",
            "font_size" : 12,
            "bold" :False
        }
    )
    worksheet.set_column(0,0,28) #Column A  
    worksheet.set_column(3,4,14) #Column D-E    
    worksheet.set_column(7,8, 14)  #Column H -I 
    worksheet.set_column(9,9, 30)  #Column J   

    for col_num, data in enumerate(header):
        worksheet.write(0,col_num,data,the_header) 
   
    sql = "SELECT * FROM resident ORDER BY court_id"
    coursor = conn.cursor()        
    coursor.execute(sql)
    result = coursor.fetchall()
    row_num = 1
    col_num = 0
    for x in result:
        firstN = x[1]
        lastN = x[2]
        renter = int(x[3])
        unitN = x[4]          
        c_id = int(x[5])
        phon = x[6]
        other = x[7]
        e_mail = x[8]   
        emer_contact = x[9]   
        person = firstN + " " + lastN
        if renter == 0:
            renter_out = " "
        else:
            renter_out = "Tenant"
        c_name = courts[c_id]
        line = [person,renter_out,unitN,c_name, "Centerville", "OH","45459",phon,other,e_mail,emer_contact]
        
        for col_num, data in enumerate(line):
            worksheet.write(row_num,col_num, data, the_body)
        row_num += 1
        col_num = 0        

        if renter > 0:            
            line = get_land_lord(renter)
            
            col_num = 0            
            worksheet.write(row_num,col_num, line[0]) 
            worksheet.write(row_num,3, line[1])
            worksheet.write(row_num,4, line[2])
            worksheet.write(row_num,5, line[3])
            worksheet.write(row_num,6, line[4])
            worksheet.write(row_num,7, line[5])
            worksheet.write(row_num,8, line[6])
            worksheet.write(row_num,9, line[7])            
            worksheet.write(row_num,10, line[8])            
            row_num += 1
    workbook.close()


write_Excel_file()
