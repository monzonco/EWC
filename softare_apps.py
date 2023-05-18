# Software Application Inventory
from tkinter import *
from tkinter import ttk
import sys
import sqlite3
from contextlib import closing
from typing import ValuesView   # use to using closing with cursor below
from report_software import *
win = Tk()
win.geometry("830x500")
win.title("Software Applications Inventory")
win.resizable(True,True)

softareN_text = StringVar()
vendor_text = StringVar()
version_text = StringVar()
website_text = StringVar()
key_license_text = StringVar()
exp_date_text = StringVar()
functionality_text = StringVar()
tips_text =  StringVar()
reference_text =StringVar()
youtube_url = StringVar()
search_text = StringVar()
apps =[]
########################### Form ###############


form_box = Frame(win, background= "white",border=5,width=600, height=630,relief="sunken",borderwidth=2)
form_box.grid(row=1, column=1,padx=10,pady=10)

####   Labels ########

softwareApp_label = ttk.Label(form_box, text= "Software App :",justify='left')
softwareApp_label.grid(row=0, column=0,sticky=W)
vendor_label = ttk.Label(form_box, text= "Vendor :",justify='left')
vendor_label.grid(row=0, column=2,sticky=W)
version_label = ttk.Label(form_box, text= "Version :",justify='left')
version_label.grid(row=1, column=0,sticky=W)
website_label = ttk.Label(form_box, text= "Website :",justify='left')
website_label.grid(row=1, column=2,sticky=W)

keylicense_label = ttk.Label(form_box, text= "Key/License :",justify='left')
keylicense_label.grid(row=2, column=0,sticky=W)

exp_date_label = ttk.Label(form_box, text= "Expiration Date :",justify='left')
exp_date_label.grid(row=2, column=2,sticky=W)

functionality_label = ttk.Label(form_box, text= "Functionality :",justify='left')
functionality_label.grid(row=3, column=0,sticky=W)
tips_label =  ttk.Label(form_box, text= "Tips :",justify='left')
tips_label.grid(row=4, column=0,sticky=W)
search_label =  ttk.Label(form_box, text= "Search :",justify = 'left')
search_label.grid(row=4, column=2,sticky=W)
reference_label =ttk.Label(form_box, text= "Reference :",justify = 'left')
reference_label.grid(row=5, column=0,sticky=W)
youtube_label = ttk.Label(form_box, text= "Youturbe URL :",justify = 'left')
youtube_label.grid(row=5, column=2,sticky=W)

######################################## text entries ##############

software_entry = Entry(form_box,width =30,borderwidth=2,textvariable=softareN_text)
software_entry.grid(row=0, column=1,padx=10,pady=10)
vendor_entry = Entry(form_box,width =30,borderwidth=2,textvariable=vendor_text)
vendor_entry.grid(row=0, column=3,padx=10,pady=10)
version_entry = Entry(form_box,width =30,borderwidth=2,textvariable=version_text)
version_entry.grid(row=1, column=1,padx=10,pady=10)
website_entry = Entry(form_box,width =30,borderwidth=2,textvariable=website_text)
website_entry.grid(row=1, column=3,padx=10,pady=10)
licence_entry = Entry(form_box,width =30,borderwidth=2,textvariable=key_license_text)
licence_entry.grid(row=2, column=1,padx=10,pady=10)

exp_date_entry =Entry(form_box,width =30,borderwidth=2,textvariable=exp_date_text) 
exp_date_entry.grid(row=2, column=3,padx=10,pady=10)
functionality_entry =Text(form_box,height=5, width=50,borderwidth=2)
functionality_entry.grid(row=3, column=1,padx=10,pady=10)
tips_entry =Text(form_box,height=5, width=50,borderwidth=2)
tips_entry.grid(row=4, column=1,padx=10,pady=10)



search_cb = ttk.Combobox(form_box,textvariable= softareN_text,values = apps)
search_cb.grid(row=4, column=3,pady=20)
#search_cb.bind('<<ComboboxSelected>>', selected)

reference_entry = Entry(form_box,width =30,borderwidth=2,textvariable=reference_text)
reference_entry.grid(row=5, column=1,padx=10,pady=10)
youtube_entry = Entry(form_box,width =30,borderwidth=2,textvariable=youtube_url)
youtube_entry.grid(row=5, column=3,padx=10,pady=10)

from sqlite3.dbapi2 import Connection
conn = sqlite3.connect('softwareApps.db')   
cursor = conn.cursor()

def add_software():
    sw_name = software_entry.get()
    sw_vendor = vendor_entry.get()  
    id =get_primarykey(sw_name,sw_vendor) 
    if id == 0:          # This software in not in database so you can add it
        sw_version = version_entry.get()
        sw_vendor_url = website_entry.get()         ## Vendor Website 
        sw_lic = licence_entry.get()                ##### key/license
        sw_expire = exp_date_entry.get()    
        sw_func   = functionality_entry.get(1.0,END)
        sw_tips   = tips_entry.get(1.0,END)  ### hint 
        sw_referral = reference_entry.get()
        sw_youtube = youtube_entry.get()
        cursor = conn.cursor()
        add_button.config(fg = "green")
    
        cursor.execute( "INSERT INTO softapp (name, vendor,version,vendorURL,key, expire, purpose, hint, referred, youtubeURL ) VALUES (?,?,?,?,?,?,?,?,?,?)",
                  (sw_name,sw_vendor, sw_version,sw_vendor_url ,sw_lic, sw_expire ,sw_func,sw_tips,sw_referral, sw_youtube) ) 
   
        cursor.close()
        conn.commit()
    else:
        add_button.config(fg = "red")

def load_cb():
    apps= []
    sql = "SELECT name FROM softapp order by name"
    cursor.execute(sql)
    result = cursor.fetchall()
    for a_name  in  result:           
           apps.append(a_name[0])
    search_cb.config(values=apps)
    

def is_ready():
    s_name = software_entry.get()
    v_name = vendor_entry.get()
    
    if len(s_name) > 3 and len(v_name) >3:             
        return True
    else:
        return False

def get_primarykey(s_name, v_name):
    if is_ready(): 
        id_int = 0
        try:
            sql_id = "SELECT app_id FROM softapp WHERE name = '" + s_name +"' and vendor = '" + v_name +"'"
            with closing(conn.cursor()) as c:
               c.execute(sql_id)
               result  = c.fetchone()
            for x in result:
               id_int = x
           
            return id_int
        except:
              f_key_int = 0
              return f_key_int
    else:        
        print("You need the first and last name.")


def delete_software():
    s_name = software_entry.get()
    v_name = vendor_entry.get()
    id = get_primarykey(s_name,v_name)
    if id > 0:
        cursor = conn.cursor()
        sql = "DELETE FROM softapp WHERE app_id = ?"
        cursor.execute(sql, (id,))
        conn.commit()
        cursor.close()
        delete_button.config(fg= 'green')
        load_cb()
    else:
        print("It is not in the database.")
        
    clear_screen()   

def update_software():
    if is_ready():
        sw_name = software_entry.get()
        sw_vendor = vendor_entry.get()              ## vendor name
        sw_version = version_entry.get()
        sw_vendor_url = website_entry.get()         ## Vendor Website 
        sw_lic = licence_entry.get()                ##### key/license
        sw_expire = exp_date_entry.get()    
        sw_func   = functionality_entry.get(1.0,END) ### functionality or purpose
        sw_tips   = tips_entry.get(1.0,END)          ### hint or tips
        sw_referral = reference_entry.get()
        sw_youtube = youtube_entry.get()
        cursor = conn.cursor()
        # id must be global to be able to change the whole record
       
        sql = """UPDATE softapp SET name = ?, vendor =?,version = ?,vendorURL = ?, key = ?,expire = ?, purpose = ?, hint = ?, referred = ?, youtubeURL =? WHERE app_id = ?"""
        cursor.execute(sql,(sw_name,sw_vendor,sw_version,sw_vendor_url,sw_lic,sw_expire,sw_func,sw_tips,sw_referral,sw_youtube,id))
        conn.commit()
        cursor.close()
        update_button.config(fg= 'green')

def clear_screen():
    load_cb()
    software_entry.delete(0,END)
    vendor_entry.delete(0,END)                ## vendor name
    version_entry.delete(0,END)
    website_entry.delete(0,END)               ## Vendor Website 
    licence_entry.delete(0,END)               ##### key/license
    exp_date_entry.delete(0,END)   
    functionality_entry.delete(1.0,END)
    tips_entry.delete(1.0,END)                ### hint 
    reference_entry.delete(0,END)  
    youtube_entry.delete(0,END)  

    add_button['state'] = 'active'
    update_button['state'] = 'active'

    report_button.config(fg= 'black')
    add_button.config(fg= 'black')
    update_button.config(fg= 'black')
    delete_button.config(fg= 'black')    

def report_inventory():
    report_button.config(fg= 'green')
    write_Software_report()   

def finish():
    sys.exit(0)

def selected(event):      
    the_name = software_entry.get()
    clear_screen()
    sql = "SELECT * FROM softapp WHERE name = ?"
    
    cursor.execute(sql,(the_name,))
    result = cursor.fetchall()
    for x in result: 
        global id      #### BIG Note: important to keep for updates when the name change.
        id = x[0]       
        softareN_text   = x[1]
        vendor_text = x[2]
        version_text = x[3]
        website_text =x[4]        
        key_license_text = x[5]
        exp_date_text = x[6]
        functionality_text = x[7]
        tips_text = x[8]
        reference_text = x[9]
        youtube_url = x[10]
        software_entry.insert(0,softareN_text)
        vendor_entry.insert(0,vendor_text)
        version_entry.insert(0,version_text)
        website_entry.insert(0,website_text)
        exp_date_entry.insert(0,exp_date_text)
        licence_entry.insert(0,key_license_text)
        functionality_entry.insert(1.0,functionality_text)
        tips_entry.insert(1.0,tips_text)
        reference_entry.insert(0,reference_text)
        youtube_entry.insert(0,youtube_url)
    
        


search_cb.bind('<<ComboboxSelected>>', selected)
command_box = Frame(win, background= "white",border=5,width=600, height=30,borderwidth=2)
command_box.grid(row=2, column=1,padx=10,pady=10)

add_button = Button(command_box, text="Add", width=10, borderwidth=2,command = add_software)
add_button.grid(row=0, column=0)

delete_button = Button(command_box, text="Delete", width=10, borderwidth=2,command = delete_software)
delete_button.grid(row=0, column=1)


update_button = Button(command_box, text= "Update",width=10,borderwidth= 2, command = update_software)
update_button.grid(row=0,column=2)

clear_button = Button(command_box,  text="Clear", width=10,borderwidth=2, command = clear_screen)
clear_button.grid(row=0,column=3)

report_button = Button(command_box,  text="Report", width=10,borderwidth=2, command = report_inventory)
report_button.grid(row=0,column=4)
finish_button = Button(command_box, text="Exit", width=10,borderwidth=2,command=finish )
finish_button.grid(row=0, column=5)
load_cb()
win.mainloop()