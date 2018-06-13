# ReachOut.cgi - processes form

import cgi
import sqlite3
import datetime

def main():
    newsfeed=[]
    db=sqlite3.connect('ReachOut.db')
    NewsUpdate=db.execute('select* from NewsUpdate')
    db.commit()
    fields=cgi.FieldStorage()    
    for i in NewsUpdate:
        print(i)
        newsfeed.append(i)
    print(newsfeed[0][0])
    print('Content-type: text/html\n\n') #specify html content
    head = '<HEAD><TITLE> News Update </TITLE></HEAD>'
    links="<div><BR><A href='ReachOut.html'>HOME</A>&nbsp;&nbsp;<A href='Volunteers.html'>VOLUNTEER</A>&nbsp;&nbsp; </div>"
    heading='<div><h1>News Update</h1></div>'
    content = '<TABLE><TR><TD>'+'Title: '+newsfeed[0][0]+':'+'</TD><BR><TD>'+newsfeed[0][1]+'</TD><BR><TD>'+'Time: '+newsfeed[0][2]+'</TR></TABLE>' 
    content1 = '<TABLE><TR><TD>'+'Title: '+newsfeed[1][0]+':'+'</TD><BR><TD>'+newsfeed[1][1]+'</TD><BR><TD>'+'Time: '+newsfeed[1][2]+'</TR></TABLE>'    
    content2 = '<TABLE><TR><TD>'+'Title: '+newsfeed[2][0]+':'+'</TD><BR><TD>'+newsfeed[2][1]+'</TD><BR><TD>'+'Time: '+newsfeed[2][2]+'</TR></TABLE>'    
    content3 = '<TABLE><TR><TD>'+'Title: '+newsfeed[3][0]+':'+'</TD><BR><TD>'+newsfeed[3][1]+'</TD><BR><TD>'+'Time:'+newsfeed[3][2]+'</TR></TABLE>'
    content4 = '<TABLE><TR><TD>'+'Title: '+newsfeed[4][0]+':'+'</TD><BR><TD>'+newsfeed[4][1]+'</TD><BR><TD>'+'Time: '+newsfeed[4][2]+'</TR></TABLE>'
    content5 = '<TABLE><TR><TD>'+'Title: '+newsfeed[5][0]+':'+'</TD><BR><TD>'+newsfeed[5][1]+'</TD><BR><TD>'+'Time: '+newsfeed[5][2]+'</TR></TABLE>'    
    body = '<BODY>'+heading+links+content+content1+content2+content3+content4+content5+'</BODY>'
    print('<HTML>' +head+body + '</HTML>')
main()


