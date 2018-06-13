import sqlite3
import datetime
import cgi

def main():
    #this section is for addbook form
    fields = cgi.FieldStorage()
    ISBN_Number= fields.getvalue('ISBN_Number')
    Title= fields.getvalue('TITLE')
    Author= fields.getvalue('AUTHOR')
    Subject= fields.getvalue('SUBJECT')
    SignUpDate= datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')
    print(ISBN_Number,Title,Author,Subject,SignUpDate)
    
    
    # writes word to file into database
    db=sqlite3.connect('Library.db')
    db.execute('insert into Book values (?,?,?,?,?)',(ISBN_Number,Title,Author,Subject,SignUpDate))
    db.commit()
    
    print('Content-type: text/html\n\n') #specify html content
    print('<HTML>')
    print('<HEAD><TITLE></TITLE><LINK rel="stylesheet" href="libstyle.css"></HEAD>')
    print('<BODY background="Images\melk_-_abbey_-_library.jpg">')
    print('<P id="header">The book has been added into database</P><BR>')    
    print('<P id="homepage"> Welcome to a World E-books></P>')
    print('<A href="homepage.cgi"><INPUT type="button" value="View Books"></A>')
    print('</BODY>')
    print('</HTML>')    
main()
