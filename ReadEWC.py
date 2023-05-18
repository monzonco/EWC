# Read EWC csv to make the table for the database
# EWC_db.db
import sqlite3
fileName = "c:\\temp\\ewc_in.csv"
f_in = open(fileName, 'r') 
fout_name = "ewcOut.csv"
f_out = open(fout_name, 'w')
primary_key = 1
while True:
    f_out.write(str(primary_key) + ",")
    line_in = f_in.readline()
    line_in.strip(",,,")
    #line_in.lstrip(",")
    if "Resident" in line_in:
        line_in = f_in.readline() 
    if "(AW" in  line_in:
        line_in = f_in.readline() 
    if "(WF" in  line_in:
           line_in = f_in.readline()    
    if "WB" in  line_in:
           line_in = f_in.readline() 
    

    line_in = line_in.replace("Ashworth Ct.,", " 1,")
    line_in = line_in.replace("Beckett Ct.,", " 2,")
    line_in = line_in.replace("Greyfield Ct.,", "3,")
    line_in = line_in.replace("Muirfield Ct.,", "4,")
    line_in = line_in.replace("Trafalgar Ct.,", "5,")
    line_in = line_in.replace("Weatherfield Ct.,", "6,")
    line_in = line_in.replace("Wembley Cr.,", "7,")

    line_in = line_in.replace("Centerville,", "")
    line_in = line_in.replace("OH,", "")
    line_in = line_in.replace("45459,","")
    
    if "tenant" in line_in:
        line_in = line_in.replace("tenant ," ,"")

    if "Clubhouse" in line_in:
        f_out.write(line_in) 
        break
        
    line_list = line_in.split(",") 
    line_list.insert(1,"0")

    if "&" in line_list[0]:
        name_list = line_list[0].split("&") 
        f_out.write(name_list[0] + ",") 
        f_out.write(name_list[1] + ",")
    else:
        name_list = line_list[0].split(" ") 
        f_out.write(name_list[0] + ",") 
        f_out.write(name_list[1] + ",")

    for x in line_list[1:9]:
        print(x)          
        f_out.write(x +",")

    
    primary_key += 1 
    f_out.write("\n")   
print("Finished")
f_in.close()
f_out.close()     

