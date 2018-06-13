#Calaculate wages
def main():
    employees=[]
    weekdays=('Monday', 'Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday')
    hours=[]
    w=0
    t=0
    while True:
        x=input("Enter name of employee (press 'enter' when done): ") #assign name of worker to variable x
        if x=='': break
        employees.append(x) #the name stored in variable x and added into list named employees
    for i in employees:
        print(i)
        w+=1
        for i in weekdays:
            print("*",i,"*")
            y=int(input("Enter hours worked by employee: "))
            hours.append(y)
            if i=='Saturday':
                hours[5*w]=(y*1.5)
            if i=='Sunday':
                hours[6*w]=(y*2)
        for i in hours:
            money=sum(hours[:6*(w+1)]) #this step is suppose to sum up the hours of each worker but i couldn't do it in time to fix it to work for each user :(
        for i in employees:
            print(i,'R',money)
            
main()