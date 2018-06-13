import sys, random
from PyQt4 import QtGui, QtCore
from GameClient import *
from SOSTextClient import SOSTextClient
from LoopThread import LoopThread
from PyQt4.phonon import Phonon
import time
import os
os.startfile('"SOSGameServer.bat"') # running bat file



class SOSGame(QtGui.QWidget,GameClient):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        GameClient.__init__(self)
        self.setGeometry(500, 75, 600, 550)    	# x,y,width,height based on screen
        self.setWindowTitle('SOS Game')
        self.resize(700, 650)
        self.setMinimumSize(460,600)
        self.setMaximumSize(900,800)
        
        self.lp = LoopThread()
    
     #labels
        self.server = QtGui.QLabel('Server:')	             # create Label, self object is parent
        self.server_ip = QtGui.QLineEdit()	             # create LineEdit, self object is parent
        self.server_ip.setPlaceholderText("Enter Server IP Address")
        self.game_title = QtGui.QLabel("SOS GAME")
        self.connect_button = QtGui.QPushButton("Connect / Disconnect")
        self.player0 = QtGui.QLabel("Player0")
        self.player1 = QtGui.QLabel("Player1")
        self.player0_score = QtGui.QLabel("Score: ")
        self.score0 = QtGui.QLabel("0",self)
        self.player1_score = QtGui.QLabel("Score: ")
        self.score1 = QtGui.QLabel("0",self)
        self.player0_turn = QtGui.QLabel("Turn: ")
        self.player0_turn_indicator = QtGui.QLabel(" --- ")
        self.player1_turn = QtGui.QLabel("Turn :")
        self.player1_turn_indicator = QtGui.QLabel(" ---")
        self.play_move_heading = QtGui.QLabel("Play Move")
        self.play_move_heading.setFont(QtGui.QFont('Arial',14))   # creating a bigger font
        self.position = QtGui.QLabel("Position: ")
        self.character = QtGui.QLabel("Character: ")
        self.game_title = QtGui.QLabel("SOS GAME")
        self.game_title.setFont(QtGui.QFont('Arial',18))   # creating a bigger font        
        self.server_messages_label = QtGui.QLabel("Server Messages")
        self.server_messages_label.setFont(QtGui.QFont('Arial',15))   # creating a bigger font        
    
      
    #Combo Boxes
        self.position_list = QtGui.QComboBox()
        self.character_list = QtGui.QComboBox()
        self.position_list.addItems(["Select Position","0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15"])   # Adding numbers onto the position combo_box
        self.character_list.addItems(["Select Character","S","O"])    # Adding characters onto the character combo_box
    
    
    #Button
        self.play_button = QtGui.QPushButton("Play")
        self.exit_button = QtGui.QPushButton("Exit")
        self.instructions = QtGui.QPushButton("Help")
        self.music_button = QtGui.QPushButton('Play Music')
        
    # Pictures of numbers on the grid
        self.no_0 = QtGui.QPixmap('numbers/0.png')
        self.no_1 = QtGui.QPixmap('numbers/1.png')
        self.no_2 = QtGui.QPixmap('numbers/2.png')
        self.no_3 = QtGui.QPixmap('numbers/3.png')
        self.no_4 = QtGui.QPixmap('numbers/4.png')
        self.no_5 = QtGui.QPixmap('numbers/5.png')
        self.no_6 = QtGui.QPixmap('numbers/6.png')
        self.no_7 = QtGui.QPixmap('numbers/7.png')
        self.no_8 = QtGui.QPixmap('numbers/8.png')
        self.no_9 = QtGui.QPixmap('numbers/9.png')
        self.no_10 = QtGui.QPixmap('numbers/10.png')
        self.no_11 = QtGui.QPixmap('numbers/11.png')
        self.no_12 = QtGui.QPixmap('numbers/12.png')
        self.no_13 = QtGui.QPixmap('numbers/13.png')
        self.no_14 = QtGui.QPixmap('numbers/14.png')
        self.no_15 = QtGui.QPixmap('numbers/15.png')
    
        # Pictures of numbers labels
        self.no_0_label = QtGui.QLabel()
        self.no_1_label = QtGui.QLabel() 
        self.no_2_label = QtGui.QLabel()
        self.no_3_label = QtGui.QLabel()
        self.no_4_label = QtGui.QLabel()
        self.no_5_label = QtGui.QLabel()
        self.no_6_label = QtGui.QLabel()         
        self.no_7_label = QtGui.QLabel() 
        self.no_8_label = QtGui.QLabel()
        self.no_9_label = QtGui.QLabel() 
        self.no_10_label = QtGui.QLabel() 
        self.no_11_label = QtGui.QLabel()
        self.no_12_label = QtGui.QLabel()
        self.no_13_label = QtGui.QLabel()
        self.no_14_label = QtGui.QLabel() 
        self.no_15_label = QtGui.QLabel() 
        
        self.no_0_label.setPixmap(self.no_0) 
        self.no_1_label.setPixmap(self.no_1)
        self.no_2_label.setPixmap(self.no_2)
        self.no_3_label.setPixmap(self.no_3)
        self.no_4_label.setPixmap(self.no_4)
        self.no_5_label.setPixmap(self.no_5)
        self.no_6_label.setPixmap(self.no_6)
        self.no_7_label.setPixmap(self.no_7)
        self.no_8_label.setPixmap(self.no_8)
        self.no_9_label.setPixmap(self.no_9)
        self.no_10_label.setPixmap(self.no_10)
        self.no_11_label.setPixmap(self.no_11)
        self.no_12_label.setPixmap(self.no_12)
        self.no_13_label.setPixmap(self.no_13)
        self.no_14_label.setPixmap(self.no_14)
        self.no_15_label.setPixmap(self.no_15)
        
    
       # Adding pictures on the grid 
        self.board_grid = QtGui.QGridLayout()
        self.board_grid.addWidget(self.no_0_label,0,0)        
        self.board_grid.addWidget(self.no_1_label,0,1)
        self.board_grid.addWidget(self.no_2_label,0,2)
        self.board_grid.addWidget(self.no_3_label,0,3)
        self.board_grid.addWidget(self.no_4_label,1,0)
        self.board_grid.addWidget(self.no_5_label,1,1)
        self.board_grid.addWidget(self.no_6_label,1,2)
        self.board_grid.addWidget(self.no_7_label,1,3)
        self.board_grid.addWidget(self.no_8_label,2,0)
        self.board_grid.addWidget(self.no_9_label,2,1)
        self.board_grid.addWidget(self.no_10_label,2,2)
        self.board_grid.addWidget(self.no_11_label,2,3)
        self.board_grid.addWidget(self.no_12_label,3,0)
        self.board_grid.addWidget(self.no_13_label,3,1)
        self.board_grid.addWidget(self.no_14_label,3,2)
        self.board_grid.addWidget(self.no_15_label,3,3)
        
        self.groupBox = QtGui.QGroupBox()
        self.groupBox.setLayout(self.board_grid)                # Adding the boarder around
        
        self.groupBox.setStyleSheet("QGroupBox {background-color: lightblue padding 6px;  border:4px solid; border-style: inset; background-image: url(images/sos_b.jpg); width}") 
    
        #music player features   
        self.media = Phonon.MediaObject(self)
        self.media.stateChanged.connect(self.handleStateChanged)            
        self.audio = Phonon.AudioOutput(Phonon.VideoCategory, self)
        Phonon.createPath(self.media, self.audio)
        self.music_button.clicked.connect(self.stopButton)          
        self.sources = []
    
    # Text_Boxes
        self.server_messages = QtGui.QListWidget(self)
    
    # Main Layout
        self.grid = QtGui.QGridLayout()
        self.grid.addWidget(self.server,0,0)
        self.grid.addWidget(self.server_ip,0,1,1,3) # setting position and size
        self.grid.addWidget(self.connect_button,0,4,1,2)
        self.grid.addWidget(self.game_title,1,2)
        self.grid.addWidget(self.player0,2,0)
        self.grid.addWidget(self.player1,2,3)
        self.grid.addWidget(self.player0_score,3,0)
        self.grid.addWidget(self.score0,3,1)
        self.grid.addWidget(self.player1_score,3,3)
        self.grid.addWidget(self.score1,3,4)
        self.grid.addWidget(self.player0_turn,4,0)
        self.grid.addWidget(self.player0_turn_indicator,4,1)
        self.grid.addWidget(self.player1_turn,4,3)   
        self.grid.addWidget(self.player1_turn_indicator,4,4)
        self.grid.addWidget(self.groupBox,5,0,6,4)
        self.grid.addWidget(self.play_move_heading,5,4)
        self.grid.addWidget(self.position,6,4)
        self.grid.addWidget(self.position_list,6,5)
        self.grid.addWidget(self.character,7,4)
        self.grid.addWidget(self.character_list,7,5)
        self.grid.addWidget(self.play_button,8,5)
        
        self.grid.addWidget(self.server_messages_label,11,2)
        self.grid.addWidget(self.server_messages,12,0,1,6)
        self.grid.addWidget(self.instructions,13,4)
        self.grid.addWidget(self.exit_button,13,5)
        self.grid.addWidget(self.music_button,13,0)
        
        self.setLayout(self.grid)  
        
    
#Customization of the gui

        #Changing labels fonts
        self.server.setFont(QtGui.QFont('Times',14,3))             # create Label, self object is parent
        self.player0.setFont(QtGui.QFont('Times',14,3))
        self.player1.setFont(QtGui.QFont('Times',14,3))
        self.player0_score.setFont(QtGui.QFont('Times',14,3))
        self.player1_score.setFont(QtGui.QFont('Times',14,3))
        self.score0.setFont(QtGui.QFont('Times',14,3))
        self.score1.setFont(QtGui.QFont('Times',14,3))
        self.player0_turn.setFont(QtGui.QFont('Times',14,3))
        self.player1_turn.setFont(QtGui.QFont('Times',14,3))
        self.player0_turn_indicator.setFont(QtGui.QFont('Times',14,3))
        self.player1_turn_indicator.setFont(QtGui.QFont('Times',14,3))
        self.play_move_heading.setFont(QtGui.QFont('Arial',14))      # creating a bigger font
        self.position.setFont(QtGui.QFont('Times',14,3))
        self.character.setFont(QtGui.QFont('Times',14,3))
        self.game_title.setFont(QtGui.QFont('Arial',20,5))             # creating a bigger font        
        self.server_messages_label.setFont(QtGui.QFont('Arial',15))   # creating a bigger font 
        
        # Changing labels colour and message boxes
        self.server.setStyleSheet("QLabel { color: white;}")
        self.player0.setStyleSheet("QLabel { color: white;}")
        self.player1.setStyleSheet("QLabel { color: white;}")
        self.player0_score.setStyleSheet("QLabel { color: white;}")
        self.player1_score.setStyleSheet("QLabel { color: white;}")
        self.score0.setStyleSheet("QLabel { color: white;}")
        self.score1.setStyleSheet("QLabel { color: white;}")
        self.player0_turn.setStyleSheet("QLabel { color: white;}")
        self.player1_turn.setStyleSheet("QLabel { color: white;}")
        self.player0_turn_indicator.setStyleSheet("QLabel { color: white;}")
        self.player1_turn_indicator.setStyleSheet("QLabel { color: white;}")
        self.play_move_heading.setStyleSheet("QLabel { color: white;}")     
        self.position.setStyleSheet("QLabel { color: white;}")
        self.character.setStyleSheet("QLabel { color: white;}")
        self.game_title.setStyleSheet("QLabel { color: white;}")
        self.server_messages_label.setStyleSheet("QLabel { color: white;}") 
        self.server_messages.setStyleSheet("QTextEdit { color: rgb(50, 50, 50); font-size: 11px; background-color: lightblue; }")
        self.server_ip.setStyleSheet("QLineEdit { color: rgb(50, 50, 50); font-size: 11px; background-color: lightblue;}")
        
        #Styling 1  comboboxs      
        QtGui.QApplication.setStyle(QtGui.QStyleFactory.create('cleanlooks')) #this changes the theme from windows 8 to more smooth good looking comboboxs

        #backgroundColor and picture
        self.picture = QtGui.QPalette(self)
        self.picture.setBrush(QtGui.QPalette.Background,QtGui.QBrush(QtGui.QPixmap('images/inclined-lines-abstract-wide-wallpaper-1600x900-004.jpg')))   
        self.setPalette(self.picture)
            
        #setting up window icon
        self.setWindowIcon(QtGui.QIcon('images/sos1.png')) 
        
         
        #pushbuttons color
        self.connect_button.setStyleSheet("QPushButton { background-color: lightgreen;}") #green button indication to proceed
        self.play_button.setStyleSheet("QPushButton { background-color: lightgreen;}") 
        self.exit_button.setStyleSheet("QPushButton { background-color: #c34242;}")          #red button to indicate stop or exit
        
    
       #connecting buttons to user interface 
        self.connect(self.connect_button,QtCore.SIGNAL('clicked()'),self.connect_server)
        self.connect(self.play_button,QtCore.SIGNAL('clicked()'),self.play_move)
        self.connect(self.exit_button,QtCore.SIGNAL('clicked()'),self.exit_game)
        self.connect(self.instructions,QtCore.SIGNAL('clicked()'),self.instruction_clicked)
        
        self.lp = LoopThread()                                           # create thread
        self.lp.update_label_signal.connect(self.loop_thread_slot)        # connect signals to slots
        

    def connect_server(self):
        self.server_messages.addItem('Trying to connect, please wait.')
        self.server_ip = self.server_ip.displayText()
        ip = self.server_ip #this is used to make name of ip to be accessible to both gui and thread class
        self.lp.connect(ip) 
        self.lp.start() # thread started    
        
    
    def loop_thread_slot(self, msg):       # slot which handles signal from thread 
        
        if msg[0:8] == 'new game':
                self.server_messages.clear()   # clears the message board when new game is played
                self.score0.setText("0")   # resetting the score when a new game is started
                self.score1.setText("0")                 
                self.player = msg[9:10]   # getting which player is player one and two
                self.server_messages.addItem("New game has been started, you are player {}.".format(msg[9:10]))
                
                # Resetting the board for a new game
                self.no_0_label.setPixmap(self.no_0) 
                self.no_1_label.setPixmap(self.no_1)
                self.no_2_label.setPixmap(self.no_2)
                self.no_3_label.setPixmap(self.no_3)
                self.no_4_label.setPixmap(self.no_4)
                self.no_5_label.setPixmap(self.no_5)
                self.no_6_label.setPixmap(self.no_6)
                self.no_7_label.setPixmap(self.no_7)
                self.no_8_label.setPixmap(self.no_8)
                self.no_9_label.setPixmap(self.no_9)
                self.no_10_label.setPixmap(self.no_10)
                self.no_11_label.setPixmap(self.no_11)
                self.no_12_label.setPixmap(self.no_12)
                self.no_13_label.setPixmap(self.no_13)
                self.no_14_label.setPixmap(self.no_14)
                self.no_15_label.setPixmap(self.no_15)
                 
                      
        elif msg[:] =='your move':
            self.message = msg
            
            # Indicating who's turn is it to play
            if self.player == '0':
                self.player0_turn_indicator.setText("Your Move")
                self.player1_turn_indicator.setText("Wait")     
            else:
                self.player0_turn_indicator.setText("Wait")
                self.player1_turn_indicator.setText("Your Move")
            
                    
        
        elif msg[:] == 'opponents move': 
            
            # Indicating who's turn is it to play
            if self.player == '0':
                self.player0_turn_indicator.setText("Wait")
                self.player1_turn_indicator.setText("Your Move")
            
            else:
                self.player0_turn_indicator.setText("Your Move")
                self.player1_turn_indicator.setText("Wait")
                
                                        
        elif msg[0:5] =='valid':                      # If the move is valid do the following
                     
            selected_move_list = msg.split(',')
            
            position = selected_move_list[1]
            character = QtGui.QPixmap('numbers/' + selected_move_list[2] + '.png')
            self.Player0_score = selected_move_list[3]
            self.Player1_score = selected_move_list[4]
            
            # Updating the scores
            self.score0.setText(self.Player0_score)
            self.score1.setText(self.Player1_score)
        
            # if the users chooses these positin replace the number with the chosen character                        
            if position == '0':
                self.no_0_label.setPixmap(character) 
                
            elif position =='1':
                self.no_1_label.setPixmap(character) 
                
            elif position =='2':
                self.no_2_label.setPixmap(character) 
                                        
            elif position =='3':
                self.no_3_label.setPixmap(character)
                
            elif position =='4':
                self.no_4_label.setPixmap(character)
                     
            elif position =='5':
                self.no_5_label.setPixmap(character)
                
            elif position =='6':
                self.no_6_label.setPixmap(character)
            
            elif position =='7':
                self.no_7_label.setPixmap(character)
                    
            elif position =='8':
                self.no_8_label.setPixmap(character)
             
            elif position =='9':
                self.no_9_label.setPixmap(character)
                
            elif position =='10':
                self.no_10_label.setPixmap(character)
                
            elif position =='11':
                self.no_11_label.setPixmap(character) 
            
            elif position =='12':
                self.no_12_label.setPixmap(character)
                     
            elif position =='13':
                self.no_13_label.setPixmap(character)
                
            elif position=='14':
                self.no_14_label.setPixmap(character)
            
            elif position =='15':
                self.no_15_label.setPixmap(character)
                  
        elif msg == 'invalid move':                 # If the selected move is invalid
            self.server_messages.addItem("Invalid move, try agian.")   
                                   
        
        elif msg[0:9] == 'game over':         # This is when the board is full
        
            winner_list = msg.split(',')      # Spliting the message into a list
            winner = winner_list[1]           # Game winner
            p0_final_score = winner_list[2]    
            p1_final_score = winner_list[3]   # Final scores
            
            if p0_final_score == p1_final_score:
                QtGui.QMessageBox.information(self, "Game over","Winner: Drawn Battle (Level Score)  \nPlayer 0 Final Score: {} \nPlayer 1 Final Score: {}".format(p0_final_score,p1_final_score))
           
            else:
                QtGui.QMessageBox.information(self, "Game over","Winner: Player {} \nPlayer 0 Final Score: {} \nPlayer 1 Final Score: {}".format(winner,p0_final_score,p1_final_score))
                
            
        elif msg == 'play again':
            
            reply = QtGui.QMessageBox.question(None,'Play Again','Do you want to play again?',QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
            
            if reply == QtGui.QMessageBox.Yes:
                x = 'y'
            
            else:
                x = 'n'
            
            
            self.lp.move(x)
            
        elif msg == 'exit game':
            self.server_messages.addItem("The game has been ended either by you or the opponent.")

    
    def instruction_clicked(self):   # Game instructions        
        instruction = QtGui.QMessageBox.information(self,"Instructions",'Connection \n \n 1.Connect to the server by entering your oppenent\'s IP ADDRESS then press the Connect/Disconnect button.\n2.Check the Server Message box to see if you are connected.\n3.Look for your player number on the Server Messages box below..\n4.If you want to quit game,press the exit button. \n \n How The Game Works \n \nPlayers take turns to add either an "S" or an "O" to any square, with no requirement to use the same letter each turn. The object of the game is for each player to attempt to create the straight sequence S-O-S among connected squares (either diagonally, horizontally, or vertically), and to create as many such sequences as they can. If a player succeeds in creating an SOS, that player immediately takes another turn, and continues to do so until no SOS can be created on their turn. Otherwise turns alternate between players after each move.')                                           
        
        
    def exit_game(self):
        
        # adding buttons to ask user if they want to quit or not
        reply = QtGui.QMessageBox.question(None,'WARNING !!','Are you sure you want exit?',QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
        
        if reply == QtGui.QMessageBox.Yes:
            self.server_messages.addItem("The oppenent has exited the game, run the game again to play new opponent")
            self.close()
       
        
    def play_move(self):
        x = self.position_list.currentText() + ',' + self.character_list.currentText()   # position and character
        
        try:
            sms = self.position_list.currentText() + ',' + self.character_list.currentText() 
            if self.message == 'your move':
                self.lp.move(sms)     # sending to the loop to send to the thread
            else:
                self.server_messages.addItem('The move cannot be played because it is not your move yet, Please wait.')
        
        except:
            self.server_messages.addItem('Error: The game is not connected, first connect to server.')  # Error if the users players before the connection is established
            
    def addFiles(self):
        files = QtGui.QFileDialog.getOpenFileNames(self, "Select Music Files",
                QtGui.QDesktopServices.storageLocation(QtGui.QDesktopServices.MusicLocation))

        if not files:
            return

        index = len(self.sources)

        for string in files:
            self.sources.append(Phonon.MediaSource(string))

        if self.sources:
            self.metaInformationResolver.setCurrentSource(self.sources[index])  
 
    def stopButton(self):
        if self.media.state() == Phonon.PlayingState: #This is to keep track of media state
            self.media.stop() #stop any media if being executed
        else:
            path = QtGui.QFileDialog.getOpenFileName(self, self.music_button.text()) #opens directry on local disk for person to select a file
            if path:
                self.media.setCurrentSource(Phonon.MediaSource(path)) # sets the media file selected so it is executed
                self.media.play()  #executes the media file
    
    def handleStateChanged(self, newstate, oldstate):
        if newstate == Phonon.PlayingState:
            self.music_button.setText('Stop') #if the play file button is clicked it changes state to allow user to stop media being played
        elif (newstate != Phonon.LoadingState and
              newstate != Phonon.BufferingState):
            self.music_button.setText('Choose File')
            if newstate == Phonon.ErrorState:
                source = self.media.currentSource().fileName()
                print ('ERROR: could not play:', source.toLocal8Bit().data())
                print ('  %s' % self.media.errorString().toLocal8Bit().data())
            
        
        
app = QtGui.QApplication(sys.argv)
abs_widget = SOSGame()
abs_widget.show()
sys.exit(app.exec_())