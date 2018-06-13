#A final mark calculator that determines where a person has passed the course or not
def course_cal():
    a=input("Enter student name: ")
    b=input("Enter student number: ")
    c=input("Enter percentage mark for programming assignment: ")
    d=input("Enter percentage mark for class tests: ")
    e=input("Enter percentage mark for final exam: ")
    f=((int(c[:-1])*0.3)+(int(d[:-1])*0.2)+(int(e[:-1])*0.5)) 
    if 75<=f<100:
        g="You have passed with 1st class grade, Excellent!"
    elif 60<=f<74.99:
        g="You have passed with 2nd class grade, Congratulations!"
    elif 50<=f<59.99:
        g="You have passed with 3rd class grade, Congratulations!"
    elif 0<=f<49.99:
        g="Fail, you have not met the minimum mark to pass the course!"
    print("***Final Mark Calculator***")
    print()
    print("Name: ",a)
    print()
    print("Student Number: ",b)
    print()
    print("Programming Assignment Mark: ",c,sep='')
    print()    
    print("Class Test Mark: ",d,sep='')
    print()    
    print("Final Mark Exam: ",e,sep='')
    print()
    print("Results:")
    print()
    print("Your final mark is ",round(f,2),"%",sep='')
    print()
    print(g)
course_cal()