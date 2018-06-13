import cgi
import sqlite3
import datetime

def main():
    
    #this section connects to database to compare username and password so it authenticates the user
    fields=cgi.FieldStorage()
    username= fields.getvalue('username')
    password= fields.getvalue('password')
    db=sqlite3.connect('Library.db')
    userinfor1=db.execute('select* from User')
    db.commit()
    for i in userinfor1:
        if i[2]==username and i[3]==password:
            print('Content-type: text/html\n\n') #specify html content
            print('<HTML>')
            print('<HEAD><TITLE></TITLE><LINK rel="stylesheet" href="libstyle.css"></HEAD>')
            print('<BODY background="melk_-_abbey_-_library.jpg">')
            print('<P id="header">You Have Successfully Logged In!</P><BR>')    
            print('<P id="homepage"> Welcome to a World E-books></P>')
            print('<A href="homepage.cgi"><INPUT type="button" value="View Books"></A>')
            print('</BODY>')
            print('</HTML>')
            break
        else:
            print('Content-type: text/html\n\n') #specify html content
            print('<HTML>')
            print('<HEAD><TITLE></TITLE><LINK rel="stylesheet" href="libstyle.css"></HEAD>')
            print('<BODY background="Images\is-this-the-best-internet-explorer-error-message-ever--12d66f9327.jpg">')
            print('<P id="homepage"> Welcome to a World E-books</P>')            
            print('<P id="header">Loging in Failed!</P><BR>')    
            print('<A href="login.html"><INPUT type="button" value="Try Again"></A>')
            print('</BODY>')
            print('</HTML>')
            break
main()