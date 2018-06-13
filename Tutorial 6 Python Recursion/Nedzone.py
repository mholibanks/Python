def factorial_loop(n): # a iterative fucntion of a factorial
    factorial=1
    if n>=0:
        for i in range(n):
            factorial*=n
            n-=1
        print(factorial)

def factorial_recursive(n): #a recursive type of factorial function
    if n<=0:
        return 1
    else:
        return n*factorial_recursive(n-1)

def main():
    n=int(input('Enter n for factorial: '))
    print(factorial_recursive(n))
    factorial_loop(n)
main()
