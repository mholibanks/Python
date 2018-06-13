# ReachOut.cgi - processes form

import cgi
import sqlite3
import datetime

def main():
    #this section is for volunteer form
    fields = cgi.FieldStorage()
    Name= fields.getvalue('Name')
    Surname= fields.getvalue('Surname')
    Address= fields.getvalue('Address')
    Telephone= fields.getvalue('Telephone')
    Email= fields.getvalue('Email')
    SignUpDate=datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')
    print(Name,Surname,Address,Telephone,Email,SignUpDate)
    
    
    # writes word to file into database
    db=sqlite3.connect('ReachOut.db')
    db.execute('insert into Volunteers values (?,?,?,?,?,?)',(Name,Surname,Address,Telephone,Email,SignUpDate))
    db.commit()
    
main()


