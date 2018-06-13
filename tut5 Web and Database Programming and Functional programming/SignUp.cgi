import sqlite3
import datetime
import cgi

def main():
    #this section is for sign up form
    fields = cgi.FieldStorage()
    name= fields.getvalue('name')
    surname= fields.getvalue('surname')
    username= fields.getvalue('username')
    password= fields.getvalue('password')
    SignUpDate=datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')
    print(name,surname,username,password)
    
    
    # writes word to file into database
    db=sqlite3.connect('Library.db')
    db.execute('insert into User values (?,?,?,?)',(name,surname,username,password))
    db.commit()
    print('Content-type: text/html\n\n') #specify html content
    print('<HTML>')
    print('<HEAD><TITLE></TITLE><LINK rel="stylesheet" href="libstyle.css"></HEAD>')
    print('<BODY background="Images\library.jpg">')
    print('<P id="homepage">Welcome to a World E-books</P><BR>')        
    print('<P id="header">Your account was successfully created!</P>') 
    print('<A href="homepage.cgi"><INPUT type="button" value="View Books"></A>')    
    print('</BODY>')
    print('</HTML>')      
main()
