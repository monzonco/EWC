from tkinter import *
import sys
import sqlite3
from contextlib import closing
from typing import ValuesView   # use to using closing with cursor below
import datetime                  #####  to use time functions

#  HTML tags
# tags used for the HTML
# Title Professional goes here
beginAnchor = " <a href=\""
endAnchor = "</a>"

p = "<p>"
endP = "</p>"

strong = "<strong>"
endStrong = "</strong>"

photoClass = "<img class=\"aligncenter size-full wp-image-170\" "
photoSource = "src=\""
window =  Tk()
window.geometry("1000x610")
window.resizable(False,False)
window.title("Professionl Counseling Services of Ohio, LLC  https://www.procounselgroup.com/")
f_name = StringVar()
l_name = StringVar()
cred_text = StringVar()
phone_text = StringVar()
photo_text = StringVar()
firstN_label = Label(window, text= "First Name")
firstN_label.grid(row=0, column=0)
firstN_entry = Entry(window, textvariable = f_name,width=15,borderwidth=2)
firstN_entry.grid(row =0, column =1,sticky=W,padx=10,pady=10)
lastN_label = Label(window, text= "Last Name")
lastN_label.grid(row=1, column= 0)
lastN_entry = Entry(window,textvariable = l_name, width=15,borderwidth=2)
lastN_entry.grid(row =1, column =1,sticky=W,padx=10,pady=10)
cred_label = Label(window, text= "Credentials")
cred_label.grid(row=2, column= 0)
cred_entry = Entry(window, textvariable =cred_text,width=15,borderwidth=2)
cred_entry.grid(row =2, column =1,sticky=W, padx=10,pady=10)
phone_label = Label(window, text="Phone Number ")
phone_label.grid(row=3, column= 0)
phone_entry = Entry(window, textvariable = phone_text,width=15,borderwidth=2)
phone_entry.grid(row =3, column =1,sticky=W,padx=10,pady=10)
photo_label = Label(window, text= "Photo Link")
photo_label.grid(row=4, column= 0)

photo_entry = Entry(window, textvariable = photo_text, width=70,borderwidth=2)
photo_entry.grid(row =4, column =1,sticky=E,padx=10,pady=10)

bio_text = StringVar()
edu_text = StringVar()
lic_text = StringVar()

bio_label = Label(window,text="Biography")
bio_label.grid(row=5, column= 0)
bio_entry = Text(window,height=5,width=100,borderwidth=2)
bio_entry.grid(row =5, column =1,padx=10,pady=10)
edu_label = Label(window, text="Education")
edu_label.grid(row=9, column= 0)
edu_entry = Text(window,height=5, width=100,borderwidth=2)
edu_entry.grid(row =9, column =1,padx=10,pady=10)

lic_label = Label(window, text="License/Awards")
lic_label.grid(row=10, column= 0)
lic_entry = Text(window,height=5, width=100,borderwidth=2)
lic_entry.grid(row =10, column =1,padx=10,pady=10)

f_key_int = 0
bios_info = ""
edu_info = ""
lic_info = ""

from sqlite3.dbapi2 import Connection
conn = sqlite3.connect('group_bios_prof.db')   
cursor = conn.cursor()
prof_key = IntVar()

def get_primarykey(f_name, l_name):
    if is_ready(): 
        f_key_int = 0
        try:
            sql_id = "SELECT prof_id FROM biosprof WHERE firstName = '" + f_name +"' and lastName = '" + l_name +"'"
            with closing(conn.cursor()) as c:
               c.execute(sql_id)
               result  = c.fetchone()
            for x in result:
               f_key_int = x
            print("the number is : " + str(f_key_int))
            return f_key_int
        except:
              f_key_int = 0
              return f_key_int
    else:        
        print("You need the first and last name.")

def add_professional():    
    run_button.config(fg= 'black')
    delete_button.config(fg='black')
    if is_ready() :
        firstN = firstN_entry.get()
        lastN  = lastN_entry.get()
        cred   = cred_entry.get()
        phone_number = phone_entry.get()
        urlPhoto = phone_entry.get()
        cursor = conn.cursor()
        cursor.execute( "INSERT INTO biosprof (firstName, lastName,credentials,phoneNumber, photoURL ) VALUES (?,?,?,?,?)",
                  (firstN ,lastN,cred,phone_number, urlPhoto) ) 
        conn.commit()
        cursor.close()
        bio_text = bio_entry.get(1.0,END)  
        edu_text = edu_entry.get(1.0,END)
        lic_text = lic_entry.get(1.0,END)

        f_key_int = get_primarykey(firstN, lastN)
        if f_key_int > 0:
            cursor = conn.cursor()
            cursor.execute( "INSERT INTO bios VALUES (?,?,?,?)",
                  (f_key_int,bio_text,edu_text,lic_text))
            conn.commit()
            cursor.close() 
            print("adding a professional")
            add_button.config(fg='green')
        else:
            add_button.config(fg='red')
    else:
        print("Enter first and last name to Add a professional")

def del_professional( ):

        if is_ready():
             firstN = firstN_entry.get()
             lastN  = lastN_entry.get()
             f_key_int = get_primarykey(firstN, lastN)
             if f_key_int > 0:
                cursor = conn.cursor()            
                sql_del_1 = "DELETE FROM bios where fKey = " + str(f_key_int)
                cursor.execute(sql_del_1)
                sql_del_2 = "DELETE FROM biosprof where prof_id  = " + str(f_key_int)
                cursor.execute(sql_del_2)
                conn.commit()
                cursor.close()
                search_button["state"] = "active"
                add_button['state'] = "active"
                clear_button['state'] ="active"
                delete_button.config(fg= 'green')
             else:
                print('That person is not in the database')
                delete_button.config(fg='red')
                search_button["state"] = "active"
                add_button['state'] = "active"

        else:
            print('That person is not in the database')
            search_button["state"] = "active"
            add_button['state'] = "active"
        print("deleting a professional")

def search_professional( ):
        run_button.config(fg= 'black')
        delete_button.config(fg='black')
        add_button.config(fg='black')
        update_button.config(fg='black')
        if is_ready():
            firstN = firstN_entry.get()
            lastN  = lastN_entry.get()
            add_button['state']=  "active"       
            delete_button['state']=  "active"   
            cred_text = ""
            phone_text = ""
            photo_text = ""
            f_key_int = 0  
            cursor = conn.cursor()
            the_sql= "SELECT prof_id, firstName, lastName, credentials, phoneNumber, photoURL FROM biosprof WHERE firstName = \'" + firstN + "\' and lastName = \'" + lastN +"\'"
                        
            row_profs = cursor.execute(the_sql)
            for result in row_profs:  
                f_key_int =result[0]        
                firstN = result[1]
                lastN = result[2]
                cred_text = result[3]
                phone_text = result[4]
                photo_text = result[5]
          
            
            cred_entry.insert(0,cred_text)
            phone_entry.insert(0,phone_text)
            photo_entry.insert(0,photo_text)

            bio_text = "*"
            edu_text = "*"
            lic_text = "*"
            if f_key_int > 0:
               the_sql_2 = "SELECT * FROM bios where fKey  = " + str(f_key_int)
               row_bios = cursor.execute(the_sql_2 )
               for descrip in row_bios:
                bio_text = descrip[1]                
                edu_text = descrip[2]                           
                lic_text  = descrip[3]
                bio_entry.insert(END,bio_text)
                edu_entry.insert(END,edu_text)
                lic_entry.insert(END,lic_text)
                search_button["state"] = "disable"
                add_button['state'] = "disable"
                delete_button['state'] = "active"
                update_button['state'] = "active"
                clear_button['state'] = "active"
            else:
                print("The person is  NOT in the database")   
                search_button["state"] = "active"
                add_button['state'] = "active"
                                    
            print("Searching for a professional")
        else:
            print("Enter the first and the last Name to SEARCH")
            search_button["state"] = "active"
            add_button['state'] = "active"
   
           

def update_professional():

    if is_ready():
        firstN = firstN_entry.get()
        lastN = lastN_entry.get()
        cred  = cred_entry.get()
        phone  = phone_entry.get()
        photo =  photo_entry.get()
        f_key_int = get_primarykey(firstN, lastN)
        if f_key_int > 0:
            with closing(conn.cursor()) as c:  
                sql_update_1 = """UPDATE biosprof SET firstName = ?, lastName = ? ,credentials = ? , phoneNumber = ? , photoURL = ? WHERE prof_id = ?"""
                c.execute(sql_update_1, (firstN,lastN,cred, phone, photo, f_key_int))
                bio_text = bio_entry.get(1.0,END)  
                edu_text = edu_entry.get(1.0,END)
                lic_text = lic_entry.get(1.0,END)
            with closing(conn.cursor()) as c:
                c.execute("""UPDATE bios SET bioDescription = ?, education = ?, license = ? where fKey = ? """,
                (bio_text, edu_text, lic_text, f_key_int))
                conn.commit()
            print("Updating a professional")
            update_button.config(fg= 'green')
        else:
            update_button.config(fg='red')

def clear_form():
    firstN_entry.delete(0,END)
    lastN_entry.delete(0,END)
    cred_entry.delete(0,END)
    phone_entry.delete(0,END)
    photo_entry.delete(0,END)
    bio_entry.delete(1.0,END)   #  Note the difference for Text widget
    edu_entry.delete(1.0,END)
    lic_entry.delete(1.0,END)
    search_button['state'] = 'active'
    add_button['state'] = 'active'
    run_button.config(fg= 'black')
    add_button.config(fg= 'black')
    update_button.config(fg= 'black')
    delete_button.config(fg= 'black')

def run_professional():
    add_button.config(fg='black')
    update_button.config(fg='black')
    delete_button.config(fg='black')
    file_name = get_file_name()
    f_out = open(file_name, 'w')
    write_title(f_out)
    write_boss(f_out)
    write_others(f_out)
    run_button.config(fg= 'green')

def write_title(f_out):
    # Title page picture
    titlePicture = "\"http://www.procounselgroup.com/wp-content/uploads/2015/03/Professionals-e1426033551708.jpg\" >"
    source = " src=\"http://www.procounselgroup.com/wp-content/uploads/2015/03/Professionals-e1426033551708-300x61.jpg\""
    sourceAttibute = " alt=\"Professionals\" width=\"300\" height=\"61\"></a></p>"    
    title_imageClass = "<img class=\"alignnone size-medium wp-image-108\" "
    line = beginAnchor + titlePicture + title_imageClass
    f_out.write(line + '\n')
    line = source + sourceAttibute
    f_out.write(line + '\n')

def write_tag(f_out,firstN):
    nameTag = "<p> <a name=\""
    endOfNameTag = "\"></a></p>"
    line = nameTag +firstN + endOfNameTag
    f_out.write(line + '\n')

def write_blue_line(f_out):
    blueLine = "http://www.procounselgroup.com/wp-content/uploads/2015/04/03AQUA.jpg\" > "
    blueLineClass = "<img class=\"alignnone size-medium wp - image - 185\" "
    blueLineSource = " src= \"http://www.procounselgroup.com/wp-content/uploads/2015/04/03AQUA-300x5.jpg\" "
    blueLineSourceAttribute = "alt=\"03AQUA\" width=\"300\" height=\"5\">"
    line = p + beginAnchor + blueLine + blueLineClass
    f_out.write(line + '\n')
    line = blueLineSource + blueLineSourceAttribute + endAnchor + endP
    f_out.write(line + '\n')    
   

def write_professional_1(row, f_out):
        
    for result in row:
        firstN = result[1]
        lastN = result[2]
        credentials = result[3]
        phoneN = result[4]
        photoLink = result[5]

    write_tag(f_out, firstN)
    write_blue_line(f_out)     
    
    ####   Professional Name and credentials  ####
    phone = "<br>Phone: "
    line = p + strong + firstN + " " + lastN+ ", " + credentials
    f_out.write(line + '\n')
    # Professional phone 
    line = phone + phoneN + endStrong + endP
    f_out.write(line + '\n')

    # Professional photography
    line = p + beginAnchor + photoLink + "\">"
    photoAttribute = "\" alt=\"" + firstN + " " + lastN +"\" width=\"200\" height=\"197\">"
    line = line + photoClass +photoSource + photoLink +photoAttribute +endAnchor +endP
    f_out.write(line + '\n')

def make_nice(bio_part, f_out):
    blockQuote = "<blockquote><p>"
    endBlockQuote = "</p></blockquote>"
    list_part = bio_part.split("$")
    for  i in list_part:
        if len(i) > 0:
            f_out.write(blockQuote + i + endBlockQuote+ '\n')

def write_professional_2(row, f_out):
    education = "<p><strong>Education</strong></p>"
    license = "<p><strong>Licenses/Certification,Awards</strong></p>"
    desc = "*"
    educ = "*"
    lic = "*"
    for result in row:
        desc = result[1]
        educ = result[2]
        lic = result[3]
    
    make_nice(desc,f_out)
    if len(educ)>2 :
        line = education   
        f_out.write(line + '\n') 
        make_nice(educ,f_out)
    if len(lic) >2:
        line = license  
        f_out.write(line + '\n') 
        make_nice(lic,f_out) 

def write_boss(f_out):
    cursor = conn.cursor()
    row_1 = cursor.execute("SELECT prof_id, firstName, lastName, credentials, phoneNumber, photoURL FROM biosprof WHERE prof_id = 1")
    write_professional_1(row_1,f_out)
    row_2 = cursor.execute("SELECT * FROM bios WHERE FkEY = 1")
    write_professional_2(row_2, f_out)

def get_primary_keys():
    # Carla is not considered because her primary  key is igual to 1
    primary_keys = list()
    row_index = cursor.execute("SELECT prof_id FROM biosprof WHERE prof_id > 1 ORDER by  firstName")

    for i in row_index:
        primary_keys.append(i) 
    return primary_keys

def write_others(f_out):
    primary_key_list = get_primary_keys()
    for x in primary_key_list:
        id = x[0]       
        the_sql= "SELECT prof_id, firstName, lastName, credentials, phoneNumber, photoURL FROM biosprof WHERE prof_id = " + str(id)      
        row_profs = cursor.execute(the_sql)
        write_professional_1(row_profs, f_out)
        row_2 = cursor.execute("SELECT * FROM bios WHERE FkEY = " + str(id))
        write_professional_2(row_2, f_out)
       
def finish():
    print("Exiting")
    sys.exit(0)


command_box = Frame(window, background= "blue",width=600, height=30)
command_box.grid(row=12, column=1,padx=10,pady=10)
add_button = Button(command_box, text="Add", state= 'active',width=10, borderwidth=2,command=add_professional)
add_button.grid(row=0, column=0)
search_button = Button(command_box, text="Search",width=10, borderwidth=2, command=search_professional)
search_button.grid(row=0, column=1)


delete_button = Button(command_box, text= "Delete",state= 'disable',width=10,borderwidth= 2,command=del_professional)
delete_button.grid(row=0,column=2)
update_button = Button(command_box, text= "Update",state= 'disable',width=10,borderwidth= 2,command=update_professional)
update_button.grid(row=0,column=3)
clear_button = Button(command_box, text= "Clear",state= 'disable',width=10,borderwidth= 2,command=clear_form)
clear_button.grid(row=0,column=4)
run_button = Button(command_box,  text="Run", width=10,borderwidth=2, command=run_professional )
run_button.grid(row=0,column=5)
finish_button = Button(command_box, text="Exit", width=10,borderwidth=2, command=finish)
finish_button.grid(row=0, column=6)

def get_file_name():
    fecha= datetime.datetime.now()
    tailYear = fecha.year
    tailMonth = fecha.month
    tailDay = fecha.day
    tailSeconds = fecha.second
    str_trail = "_" + str(tailYear) + "_" + str(tailMonth) + "_" + str(tailDay) + "_" + str(tailSeconds) + ".html"
    fileName = "c:\\temp\\bioProfessionals" + str_trail
    return fileName

def is_ready():
    ft_name = firstN_entry.get()
    lt_name = lastN_entry.get()
    
    if len(ft_name) > 2 and len(lt_name) >2:             
        return True
    else:
        return False

window.mainloop()