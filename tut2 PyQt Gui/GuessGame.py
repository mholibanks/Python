#creating a widget app
import sys
from PyQt4 import QtGui, QtCore
import random

class GuessWidget(QtGui.QWidget):
    
    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.setGeometry(290,180,450,300)
        
        self.setWindowTitle('Guessing Game')
        #creating widgets to be added to the vbox in column 1
        self.guess=QtGui.QLabel('Guess: ')
        self.guess.setFont(QtGui.QFont('Arial',15,2))
        self.guess1=QtGui.QLabel('Guess 1:')
        self.guess2=QtGui.QLabel('Guess 2:')
        self.guess3=QtGui.QLabel('Guess 3:')
        self.space=QtGui.QLabel(' ')
        self.interface=QtGui.QLabel('Interface: ')
        self.interface.setFont(QtGui.QFont('Arial',15,2))
        self.picture=QtGui.QLabel('Picture: ')
        self.colour=QtGui.QLabel('Colour:')     
        
        self.newgame=QtGui.QPushButton('New Game')
        self.newgame.setMaximumSize(75,25)   
        
        self.Guess=QtGui.QPushButton('Guess')
        self.Guess.setMaximumSize(75,25)
        
        self.change=QtGui.QPushButton('Change')
        self.change.setMaximumSize(75,25)
        
        self.Close=QtGui.QPushButton('Close')
        self.Close.setMaximumSize(75,25)           
        
        #adding comboboxs 
        self.color_sel=QtGui.QComboBox()
        self.color_sel.addItem('red')
        self.color_sel.addItem('blue')
        self.text1=self.color_sel.currentText()        
        
        #creating a picture
        self.pic_sel=QtGui.QComboBox()
        self.pic_sel.addItem('mickey')
        self.pic_sel.addItem('pluto')
        self.text2=self.pic_sel.currentText()
        
        
        self.pixmap=QtGui.QPixmap(self.text2+'.gif')
        self.pic=QtGui.QLabel()
        self.pic.setPixmap(self.pixmap)
        
        #creating widgets to be added to the vbox in column 2
        self.edit = QtGui.QLineEdit(self)
        self.edit.setGeometry(100,50,50,20)       
        
        #colour change in the background
        self.setPalette(QtGui.QPalette(QtGui.QColor('red')))
        self.setAutoFillBackground(True)
        
        #creating the vbox for the widgets in 1st column
        self.grid=QtGui.QGridLayout()       
        self.grid.addWidget(self.pic,0,0,0,1)
        self.grid.addWidget(self.guess,1,1)
        self.grid.addWidget(self.guess1,2,1)
        self.grid.addWidget(self.guess2,3,1)
        self.grid.addWidget(self.guess3,4,1)
        self.grid.addWidget(self.space,5,1)
        self.grid.addWidget(self.interface,6,1)
        self.grid.addWidget(self.picture,7,1)
        self.grid.addWidget(self.colour,8,1)
        self.grid.addWidget(self.Close,9,1)
        self.grid.addWidget(self.edit,5,2)
        self.grid.addWidget(self.Guess,5,3)
        self.grid.addWidget(self.change,8,3)
        self.grid.addWidget(self.newgame,9,2)
        self.grid.addWidget(self.color_sel,8,2)
        self.grid.addWidget(self.pic_sel,7,2)
        self.setLayout(self.grid)  
            
        #connecting buttons to in user interface 
        self.connect(self.Guess,QtCore.SIGNAL('clicked()'),self.guess_game)
        
        self.connect(self.change,QtCore.SIGNAL('clicked()'),self.change_color)
        
        self.connect(self.change,QtCore.SIGNAL('clicked()'),self.change_pic)
        
        self.connect(self.Close,QtCore.SIGNAL('clicked()'),self.closegame)
        
        self.connect(self.newgame,QtCore.SIGNAL('clicked()'),self.newgame1)
        
        self.y=random.randint(1,10)
        self.no_of_guesses=0
        
    def guess_game(self):
        self.text3=self.edit.displayText()
        self.text3_label=QtGui.QLabel(self.text3)
        print(self.text3)
        
        if int(self.text3)==self.y:
            self.result='Correct!'
        elif int(self.text3)>self.y:
            self.result='Too Big'
        elif int(self.text3)<self.y:
            self.result='Too Small'
        
        self.result_label=QtGui.QLabel(self.result)
        
        if self.no_of_guesses==0:
            self.grid.addWidget(self.text3_label,2,2)
            self.grid.addWidget(self.result_label,2,3)
            
        elif self.no_of_guesses==1:
            self.grid.addWidget(self.text3_label,3,2)
            self.grid.addWidget(self.result_label,3,3)
            
        elif self.no_of_guesses==2:
            self.grid.addWidget(self.text3_label,4,2)
            self.grid.addWidget(self.result_label,4,3)
            
        self.no_of_guesses+=1
        
    
    def change_color(self): #change color in background
        self.text1=self.color_sel.currentText()
        self.setPalette(QtGui.QPalette(QtGui.QColor(self.text1)))
        self.setAutoFillBackground(True) 
        
    def change_pic(self):
        
        if self.text2=='pluto':
            self.grid.removeWidget(self.pic)
            self.pic.deleteLater()
            
            self.text2=self.pic_sel.currentText()        
            self.pixmap=QtGui.QPixmap(self.text2+'.gif')
            self.pic=QtGui.QLabel()
            self.pic.setPixmap(self.pixmap)
            self.grid.addWidget(self.pic,0,0,0,1)
        
        elif self.text2=='mickey':
            self.grid.removeWidget(self.pic)
            self.pic.deleteLater()
            
            self.text2=self.pic_sel.currentText()        
            self.pixmap=QtGui.QPixmap(self.text2+'.gif')
            self.pic=QtGui.QLabel()
            self.pic.setPixmap(self.pixmap)
            self.grid.addWidget(self.pic,0,0,0,1)
    
    def newgame1(self): #this is for new game button to start another game
        my_widget=GuessWidget()
        my_widget.show()
        sys.exit(my_widget.exec_()) #this is to call the function again
        sys.exit(0)
        
    def closegame(self): #this is for close button to close the game window when done playing
        self.close()          
   
app=QtGui.QApplication(sys.argv)
my_widget=GuessWidget()
my_widget.show()
sys.exit(app.exec_())
