#This script read a file that contains the list of my albums
# in flickr.com and then stored the information in a cvs file
import sys

myalbum = open('hotmail_albums.txt')
albums = myalbum.readlines()

#myalbums_2 = open('gmail_albums.txt')
#albums_2 = myalbums_2.readlines()

outputfile = open('output.csv', 'w', newline='\n')
#outputwriter = csv.writer(outputfile)
outputfile.write( "Album, Items\n")
counter = 1
album = ""
item = ""
for line in albums: 
    if counter%2 != 0:        
        n = line.find('\n') # get rid of the end of the line character
        album = line[:n]    
        album = album.replace(",","-")  #to get rid of the "," y replace it with "-"
    if counter%2 == 0:
        n = line.find('items')
        item = line[:n]            
        if len(album) > 2 and len(item) > 1:
            result = album + "," + item + "\n" 
            outputfile.write(result)
            album = ""
            item = ""
           
    counter = counter +1
    

outputfile.close()
myalbum.close()
#myalbums_2.close()
