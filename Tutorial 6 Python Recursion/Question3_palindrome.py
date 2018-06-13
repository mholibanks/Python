def palindrome(s): #definition of the program
        s.lower() #cast input string into lower
        if len(s)==0:   # base case
                return s
        else:
                return palindrome(s[1:]) +s[0] #this part reverses the string
                
def main():#main function
        x=input('Enter a sentence or word: ')
        x.lower()
        palindrome(x)
        if x==palindrome(x):
                print('Good palindrome!')
        else:
                print('Not a palindrome!')
main()