
# import the module for databases
import sqlite3

#create a database and save that connection as the token 'conn'
conn = sqlite3.connect('myDB.db')

#while the connction is open...
with conn:
    cur = conn.cursor()
    # using SQL language (CREATE TABLE to create a table if it doesn't
    # already exist; the \ allows you to continue code on next line for clarity
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        filename TEXT \
        )")
    # commit the changes
    conn.commit()
# close the connection
conn.close()



# open connection again (could make a function so we don't have to keep writing all of this
conn = sqlite3.connect('myDB.db')

# the tuple to be scanned
fileList = ('information.docx', 'Hello.txt', 'myImage.png', 'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')

#insert txt files into table then print
for x in fileList:
    if x.endswith('.txt'):
        with conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO tbl_files(filename) VALUES (?)", (x,))
            print(x)
#close the connection
conn.close()






