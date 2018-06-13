#A program that solves quadratic equation
#Mholi Mncube
#created 1 May 2014 modified 7 May 2014
def quad_solve():
    import math
    a=int(input("Enter the value of a: "))
    b=int(input("Enter the value of b: "))
    c=int(input("Enter the value of c: "))
    d=b**2-4*a*c
    if d>0:
        print("The first root is: ",int(round(((-b)+(math.sqrt(b**2-4*a*c)))/2*a,1)))
        print("The second root is: ",int(round(((-b)-(math.sqrt(b**2-4*a*c)))/2*a,1)))
    else:
        d<0
        print("There are no real roots, which simply means your function does not cut the x-axis:")
quad_solve()
q=input("Press enter to exit.")
