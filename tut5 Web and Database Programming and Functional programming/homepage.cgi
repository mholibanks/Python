import sqlite3
import cgi

def main():
    books=[]
    db=sqlite3.connect('Library.db')
    books1=db.execute('select* from Book Order by EntryTimestamp')
    db.commit()
    fields=cgi.FieldStorage()    
    for i in books1:
        print(i)
        books.append(i)
    print(books)
    
    print('Content-type: text/html\n\n') #specify html content
    print('<HTML>')
    print('<HEAD><TITLE> Home Page </TITLE><LINK rel="stylesheet" href="libstyle.css"></HEAD>')
    print('<BODY background="Images\melk_-_abbey_-_library.jpg">')
    print('<BR><A id="header" href="AddBook.html">Add a Book</A>')    
    print('<P id="homepage" Welcome to a World E-books></P>')
    print('<table id="booktable" align = "center"><BR> <tr> <th> ISBN NUMBER</th><th> TITLE </th><th>AUTHOR</th><th>SUBJECT</th><th>DATE TIME</th></tr>')
    for i in books:
        print('<tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>'.format(i[0],i[1],i[2],i[3],i[4]))  
    print('</BODY>')
    print('</HTML>')
main()