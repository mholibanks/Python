def count_element(e,s): #main function with two arguments
    if len(s)==0: #base case
        return 0
    elif e!=s[0]: #this part compares e argu with first element in the sequence if they equal it'll add
        return 0+count_element(e,s[1:]) #this changes the intial point of the indexing if e does not match with object in position
    else:
        return 1+count_element(e,s[2:]) #this does the same thing with the above comment but in the opposit when e matchs element in seqeuence
    
def main(): #defining a main function then calling the defined functions above
    e=input('Enter a an element: ')
    s=input('Enter a sequence: ')
    print(count_element(e,s))
main()