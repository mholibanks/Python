from GameClient import *

class SOSTextClient(GameClient):

    def __init__(self):
        GameClient.__init__(self)
        self.board = [' '] * BOARD_SIZE
        
    def clear_board(self):
        self.board = [' '] * BOARD_SIZE
        
    def input_server(self):
        return input('enter server:')
     
    def input_move(self):
        return input('enter position(0-15):') + ',' + input('enter char(S,O):')
     
    def input_play_again(self):
        return input('play again(y/n):')
    
    def display_board(self):
        
        if self.message[0:8] == 'new game':
            self.board_list = [[0,1,2,3],[4,5,6,7],[8,9,10,11],[12,13,14,15]]             # Initializing the board for the begining of the game.
            
        print("-"*21)                                                        # putting the linesNen on the interface            
        for i in self.board_list:                                                     # iterating through the list
            print("| {:2} | {:2} | {:2} | {:2} |".format(i[0], i[1], i[2], i[3]))   # adding the numbers as positions     
            print("-"*21)                                                        # putting the lines on the interface            

    def handle_message(self,msg):
         
        if msg[0:8] == 'new game':
            self.message = msg
            print("\nNew game has been started.")
        
        elif msg[:] =='your move':
            self.display_board()           # Displaying the board
            print("Your move.")
            y = self.input_move().split(',')         # Getting the position and character from the user and assigning them to x
            x=y[0]+','+y[1].upper() #change char input into caps to be handled by the input move function
            self.send_message(x)          # sending the message to the server
            
        elif msg[:] == 'opponents move':  
            self.display_board()                     # Displaying the board
            print("Opponents move, please wait.")    # Telling player its not yetb their time to play
            
        elif msg[0:5] =='valid':                      # If the move is valid do the following
                    
                    selected_move_list = msg.split(',')
                    self.message = msg        # This is to cahnge the elements in the board if the move is valid
                    
                    position = selected_move_list[1]
                    character = selected_move_list[2]
                    self.Player0_score = selected_move_list[3]
                    self.Player1_score = selected_move_list[4]
                    
                    #print(position , character, Player0_score, Player1_score)
                    print("Player 0 Score: {} ,Player 1 Score: {}".format(self.Player0_score, self.Player1_score)) # Displaying the scores after every move
                   
                        
                    # if the users chooses these positin replace the number with the chosen character 
                        
                    if position == '0':
                        self.board_list[0][0] = character 
                        
                    elif position =='1':
                        self.board_list[0][1] = character
                        
                    elif position =='2':
                        self.board_list[0][2] = character
                                                
                    elif position =='3':
                        self.board_list[0][3] = character 
                    
                    elif position =='4':
                        self.board_list[1][0] = character                
                             
                    elif position =='5':
                        self.board_list[1][1] = character  
                        
                    elif position =='6':
                        self.board_list[1][2] = character                                                         
                    
                    elif position =='7':
                        self.board_list[1][3] = character                
                            
                    elif position =='8':
                        self.board_list[2][0] = character                
                     
                    elif position =='9':
                        self.board_list[2][1] = character
                        
                    elif position =='10':
                        self.board_list[2][2] = character
                        
                    elif position =='11':
                        self.board_list[2][3] = character 
                    
                    elif position =='12':
                        self.board_list[3][0] = character                
                             
                    elif position =='13':
                        self.board_list[3][1] = character  
                        
                    elif position=='14':
                        self.board_list[3][2] = character                                                         
                    
                    elif position =='15':
                        self.board_list[3][3] = character                                               
                        
        elif msg == 'invalid move':                 # If the selected move is invalid
                    print("Invalid move, try agian.")   
                    
        
        elif msg[0:9] == 'game over':         # This is when the board is full
        
            winner_list = msg.split(',')      # Spliting the message into a list
            winner = winner_list[1]           # Game winner
            p0_final_score = winner_list[2]    
            p1_final_score = winner_list[3]   # Final scores
            print("Game over. \nWinner: Player {} \nPlay 0 Final Score: {} \nPlayer 1 Final Score: {}".format(winner,p0_final_score,p1_final_score)) # printing results           
        
        elif msg == 'play again':
            
            y = self.input_play_again()    # asking the user if they want to play again  
            x=y.lower()
            self.send_message(x)
     
        elif msg == 'exit game':
            print("The game has been ended either by you or the opponent.")
            
            
            
    def play_loop(self):
        try:
            while True:
                msg = self.receive_message()
                if len(msg): self.handle_message(msg)
                else: break
        except Exception as e:
            print('ERROR:' + str(e) + '\n')
            self.log('ERROR:' + str(e) + '\n')
            
def main():
    stc = SOSTextClient()
    while True:
        try:
            stc.connect_to_server(stc.input_server())
            break
        except Exception as e:
            print('Error connecting to server!\nERROR:' + str(e) + '\n')
            self.log('Error connecting to server!\nERROR:' + str(e) + '\n')
            
    stc.play_loop()
    input('Press enter to exit.')
        
#main()