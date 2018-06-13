#A program that determines whether a year is a leap year or not
#Mholi Mncube
#7/03/2014

def leap_year():
    a=eval(input("Enter a year: \n"))
    b=400
    c=4
    e=100
    if a%b==0:
        print(a,"is a leap year.\n")        
    elif a==2100:
        print(a,"is not a leap year.\n") 
    elif a%c==0:
        print(a,"is a leap year.")
    else:
        print(a,"is not a leap year.")
leap_year()