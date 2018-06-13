def sum_to_n(n): #definition of a function
    if n<=0: #base case
        return 0
    else:
        return n+sum_to_n(n-1) #this part of the function calculates the sum sum

def main(): #main function that calls the function that calculates the sum
    n=int(input('Enter number you want some of: '))
    print(sum_to_n(n))
main()