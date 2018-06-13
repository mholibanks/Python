#A program that determines where a year is leap or not
def leap_year():
    a=int(input("Enter number of month (1 January): "))
    b=int(input("Enter year: "))
    months=["December","January","February","March","April","May","June","July","August","September","October","November","December"]
    if a==1 or a==3 or a==5 or a==7 or a==9 or a==11:
        c="31"
    elif a==4 or a==6 or a==8 or a==10 or a==12:
        c="30"
    else:
        a==2
        c="29"
    if b%400==0 or b%4==0:
        print("The year,",b,months[a],"has",c,"days.")
    else:
        b%400!=0 or b%4!=0
        print("The year,",b,months[a],"has",c,"days.")   
leap_year()