import sqlite3
import sys
from PyQt4 import QtGui, QtCore
db=sqlite3.connect('database_A.db')
employees=db.execute('select*from Employee')



class EmployeeDatabase(QtGui.QWidget):
    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.setGeometry(450,250,450,400)
        self.setWindowTitle('Employee Database Management')
        
        #setting up the design of parent widget
        self.label=QtGui.QLabel('Employee:')
        
        self.client=QtGui.QLabel('Client name:')
        self.client1=QtGui.QLineEdit()
        self.client2=self.client1.displayText()
        
        self.hours=QtGui.QLabel('Number of hours:')
        self.hours1=QtGui.QLineEdit()
        self.hours2=self.hours1.displayText()   
        
        #setting up combobox
        self.combo=QtGui.QComboBox()
        self.combo.addItem('Mholi')
        self.combo.addItem('Ntuthuko')
        self.combo.addItem('Samkelisiwe')
        self.combo.addItem('Wandile')
        self.combo.addItem('Mnotho')
        self.combo.addItem('Sboniso')
        self.combo.addItem('Andreas')
        self.combo.addItem('Sqalo')
        self.combo.addItem('Sandile')
        self.combo.addItem('Mpumelelo')
        #self.text=self.combo.currentText()
        
        #pushbuttons
        self.close1=QtGui.QPushButton('Close')
        self.addtask=QtGui.QPushButton('Add Task')
        self.clear1=QtGui.QPushButton('Clear')
        self.billreport=QtGui.QPushButton('Bill Report')
        
        
        #setting up my parent widget with grid
        self.grid=QtGui.QGridLayout()
        self.grid.addWidget(self.label,1,1)
        self.grid.addWidget(self.combo,1,2)
        self.grid.addWidget(self.client,2,1)
        self.grid.addWidget(self.client1,2,2)
        self.grid.addWidget(self.hours,3,1)
        self.grid.addWidget(self.hours1,3,2)
        self.grid.addWidget(self.addtask,5,3)
        self.grid.addWidget(self.clear1,5,4)
        self.grid.addWidget(self.billreport,6,3,1,2)
        self.grid.addWidget(self.close1,7,5)
        self.setLayout(self.grid)
        
        #connecting buttons to database
        self.connect(self.close1,QtCore.SIGNAL('clicked()'),self.CloseApp)
        self.connect(self.addtask,QtCore.SIGNAL('clicked()'),self.AddTask)
        self.connect(self.clear1,QtCore.SIGNAL('clicked()'),self.ClearInterface)    
        self.connect(self.billreport,QtCore.SIGNAL('clicked()'),self.BillReport)
        
    def BillReport(self):
        import sqlite3
        from PyQt4 import QtCore, QtGui
        self.billreport1=QtGui.QMessageBox()
        self.billreport1.setWindowTitle('Billing Report')
        db=sqlite3.connect('database_A.db')
        self.EmployeeT=db.execute('select* from Employee inner join Task on EmployeeNumber1=EmployeeNumber') #this inner joins tables employee and task
        self.lst=[]
        for i in self.EmployeeT: #this section is where the billing of the worker is reported and put into a dialog box
            #print(i) #this is used for debugging purposes
            self.lst.append('Name,Surname: '+str(i[1:3])+' HoursWorked: '+str(i[6])+' TotalBillibleAmount: R'+str(i[3]*i[6]))
            self.billreport1.setInformativeText(str(self.lst))
        self.billreport1.exec_()
        
    def ClearInterface(self):
        self.hours1.clear()
        self.client1.clear()
        
    def AddTask(self):
        #this part is to get time and date
        import datetime
        self.date_time=datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')
        self.hours2=self.hours1.displayText()
        self.client2=self.client1.displayText()
        
        #this section is to get employee number
        self.text=self.combo.currentText()
        self.employees=db.execute('select*from Employee')
        for i in self.employees:
            if i[1]==self.text:
                self.employee_num=i[0]
                #print(self.employee_num) 
        
        #this section is for taskcode:
        import random
        self.taskcode=['ACC093','ECO102','STAT01','MAT409','HR0114','CEO783','STO984','MAN673','TRD231','PYS782','DOC233']
        self.y=random.randint(0,11)
                
        db.execute('insert into Task values(?,?,?,?,?,?)',(self.taskcode[self.y],self.client2,self.hours2,self.employee_num,self.date_time[0:11],self.date_time[11:]))
        db.commit()
        
    def CloseApp(self):
        self.close()
        db.close()
        
        
app=QtGui.QApplication(sys.argv)
my_widget=EmployeeDatabase()
my_widget.show()
sys.exit(app.exec_())