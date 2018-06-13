num_list = [ ]
while len(num_list)==0:
        try:
                filename = input('Enter filename:')
                file = open(filename,'r')
                
                while True:
                        line = file.readline()
                        if len(line) == 0: break
                        num = int(line)
                        num_list.append(num)
                file.close()
        except FileNotFoundError as ve:
                print('This FileNotFoundError occured,',ve)
                
        finally:
                if len(num_list)!=0:
                        while True:
                                try:    
                                        index = int(input("Enter number's index(-1 to exit):"))
                                        if index == -1: break
                                        print('Num at position',index,'is',num_list[index])                
                                except IndexError as ve:
                                        print('This IndexError occured',ve)
                                except TypeError as ve:
                                        print('This TypeError occured',ve)
                                except ValueError as ve:
                                        print('This ValueError occured.',ve)
                                except:
                                        print('Some unknown error occured.')
                
                
