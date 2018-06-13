def some_func_recur(n): #this is the recursive function of the given loop equivalent below
    if n<=1:
        return 0
    else:
        return (n*2)+some_func_recur(n//2)

def some_func(n): #this is the loop function that's an equivalent to the recursive function above
    ans = 0
    while n>1:
        ans += n*2
        n //= 2
    return ans

def main(): #main function that calls both functions and see that they both factorials
    n=int(input('Enter n: '))
    print(some_func_recur(n))
    print(some_func(n))
main()


