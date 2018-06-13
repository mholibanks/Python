def studentRegistration(name,surname): #function that creates a student name
    namee='' #empty strings store name and surname
    surnamee=''
    vowel=['a','e','i','o','u'] #list for vowels which is used to check if name or surname has vowels
    for i in name: #rthis loop iterates through the name and checks if there are vowels and collects consonants into name string
        if i in vowel: continue
        else:
            namee+=i
            x=namee.upper()
            if len(x)<1: #this checks if the name string has consosants if it has less non it just adds 3 XXX as indicated in question if necessary 
                x+='XXX'
            elif len(x)<2:
                x+='XX'
            elif len(x)<3:
                x+='X'            
    for j in surname:
        if j in vowel: continue
        else:
            surnamee+=j
            y=surnamee.upper()
            if len(y)<1:
                y+='XXX'
            elif len(y)<2:
                y+='XX'
            elif len(y)<3:
                y+='X'  
    print(y[:3]+x[:3]+'001')
def main(): #this is the main function which calls the student function above
    name=input('Enter name: ')
    surname=input('Enter surname: ')
    studentRegistration(name,surname)
main()