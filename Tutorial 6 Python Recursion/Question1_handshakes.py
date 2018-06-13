def handshakes(n): #definition of a fucntion
    if n<=1: #base case, if there's one person there can't be a handshake
        return 0
    else:
        return (n-1)+handshakes(n-1) #the function calculates the number of handshakes

def main():
    n=int(input('Enter a number of people: '))
    print(handshakes(n))
main()