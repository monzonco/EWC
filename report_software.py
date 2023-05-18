from ctypes import LittleEndianStructure
from os import linesep
import sqlite3
from contextlib import closing, nullcontext
import sys
import datetime

import xlsxwriter as xw

from xlsxwriter import Workbook
from sqlite3.dbapi2 import Connection

conn = sqlite3.connect("d:\\python_work\\softwareApps.db")   
cursor = conn.cursor() 

def get_file_name():
    fecha= datetime.datetime.now()
    tailYear = fecha.year
    tailMonth = fecha.month
    tailDay = fecha.day
    tailSeconds = fecha.second
    str_trail = "_" + str(tailYear) + "_" + str(tailMonth) + "_" + str(tailDay) + "_" + str(tailSeconds) + ".xlsx"
    fileName = "c:\\temp\\SoftwareReport" + str_trail
    return fileName

    
def write_Software_report():    
    file_name = get_file_name()
    header =['Name','Vendor', 'Version', 'Website','Key/Licence','Expiration Date','Functionality','Tips','Reference','Youtube URL']
    workbook = Workbook(file_name)
    worksheet = workbook.add_worksheet("Softwar Report")
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
    worksheet.set_column(0,0,15) #Column A  
    worksheet.set_column(1,3,12) #Column B-D    
    worksheet.set_column(4,4,38)  #Column E
    worksheet.set_column(5,5,16)  #Column F  #expiration date
    worksheet.set_column(6,7, 30)  #Column G-H 
    worksheet.set_column(8,10, 12)  #Column I-J 


    for col_num, data in enumerate(header):
        worksheet.write(0,col_num,data,the_header) 
   
    sql = "SELECT * FROM softapp ORDER BY name"
    coursor = conn.cursor()        
    coursor.execute(sql)
    result = coursor.fetchall()
    row_num = 1
    col_num = 0
    for x in result:        
        softareN_text   = x[1]
        vendor_text = x[2]
        version_text = x[3]
        website_text =x[4]        
        key_license_text = x[5]
        if key_license_text is None:
           key_license_text = "*"
        exp_date_text = x[6]
        if len(exp_date_text) <3:
            exp_date_text = "Never"
        functionality_text = x[7]
        tips_text = x[8]
        reference_text = x[9]
        youtube_url = x[10]
        line = [softareN_text,vendor_text,version_text,website_text,key_license_text,exp_date_text,functionality_text,tips_text,reference_text, youtube_url] #, "Centerville", "OH","45459",phon,other,e_mail,emer_contact]
        
        for col_num, data in enumerate(line):
            worksheet.write(row_num,col_num, data, the_body)     
        row_num += 1

    workbook.close()
#write_Software_report()
