def filescrape():
    words=[]
    numbers=[]
    report=[]
    while len(words)==0 and len(numbers)==0: #this well is the condition that allows one to re-enter the filename if they entered it wrong first time
        try: #this section of the code handles any exceptions 
            filename=input('Enter name of file: ')
            f=open(filename,'r')
        except FileNotFoundError as ve:
            print('This FileNotFoundError occured.',ve)
        except ValueError as ve:
            print('This ValueError occured.',ve)
        except TypeError as ve:
            print('This TypeError occured.',ve)
        else:
            for i in f:
                y=f.read()
                x=y.split()
                for j in x:
                    if j.isnumeric():  #all that's left evaluating strings from int type then ul ne fiished
                        numbers.append(j) #this is used to control the iteration for the continuation of the prompt when the user enters wrong username file
                        #for l in numbers:
                        f=open('numbers.txt','a')
                        f.write(j+'\n')
                    elif j.isalpha():
                        words.append(j) #this is used to control the iteration for the continuation of the prompt when the user enters wrong username file
                        #for k in words:
                        f=open('words.txt','a')
                        f.write(j+'\n')
                f=open('report.txt','a')
                f.write('The number of words in the sample file are '+str(len(words))+' and numbers are '+str(len(numbers)))
            #print(words, numbers)                   # This line used to check that the conditions in loops work
filescrape()