#tic tac toe
def OXO(): 
          OXO=[['1','2','3'],['4','5','6'],['7','8','9']] #this is the 2d list
          print(OXO[0][0],OXO[0][1],OXO[0][2],sep='|') #basically this is the grid formmated as asked in the question
          print("------")     
          print(OXO[1][0],OXO[1][1],OXO[1][2],sep='|')    
          print("------")          
          print(OXO[2][0],OXO[2][1],OXO[2][2],sep='|')
          
          for i in range(7): #this is a loop to allow players to continue play unil one has three matching lines of x or o
                    x=int(input("Player X, enter your position: ")) #prompt user to enter position to insert x
                    if x==1:
                              OXO[0][0]='X'
                    if x==2:
                              OXO[0][1]='X'                           
                    if x==3:
                              OXO[0][2]='X'
                    if x==4:
                              OXO[1][0]='X'          
                    if x==5:
                              OXO[1][1]='X'
                    if x==6:
                              OXO[1][2]='X'
                    if x==7:
                              OXO[2][0]='X'
                    if x==8: 
                              OXO[2][1]='X'
                    if x==9:
                              OXO[2][2]='X'
                    print(OXO[0][0],OXO[0][1],OXO[0][2],sep='|') #displays the new board when x has played
                    print("------")     
                    print(OXO[1][0],OXO[1][1],OXO[1][2],sep='|')    
                    print("------")          
                    print(OXO[2][0],OXO[2][1],OXO[2][2],sep='|')
                    o=int(input("Player O, enter your position: "))
                    if o==x: #this is to stop player o from placing o in position where x exists...so brekats the game start again
                              print("Invalid move")
                              break
                    if o==1:
                              OXO[0][0]='O'
                    if o==2:
                              OXO[0][1]='O'                           
                    if o==3:
                              OXO[0][2]='O' #seperate codes of lines allow alternate plays for each player
                    if o==4:
                              OXO[1][0]='O'          
                    if o==5:
                              OXO[1][1]='O'
                    if o==6:
                              OXO[1][2]='O'
                    if o==7:
                              OXO[2][0]='O'
                    if o==8: 
                              OXO[2][1]='O'
                    if o==9:
                              OXO[2][2]='O'
                    print(OXO[0][0],OXO[0][1],OXO[0][2],sep='|') #this displays board after player o has played
                    print("------")     
                    print(OXO[1][0],OXO[1][1],OXO[1][2],sep='|')    
                    print("------")          
                    print(OXO[2][0],OXO[2][1],OXO[2][2],sep='|')
          
OXO()