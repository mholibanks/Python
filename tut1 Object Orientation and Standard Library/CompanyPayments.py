#A program that will be responsible for capturing employee payment data
#23 Feb 2015
from WagedEmployee import WagedEmployee
from SalariedEmployee import SalariedEmployee
from Employee import Employee
from Person import Person



def main():                                                           #this is the main program where the classes are used
    salaried_employees=[]                                             #this is an empty list 
    waged_employees=[]
    employees=[salaried_employees,waged_employees]                    #nested lists, called arrays
    while True:
        menu=['1: Add salaried employees','2: Add waged employees','3: Display salaried employees','4: Dislay waged employees','5: Display all employees','6: Search for employee','7: Quit']
        print()
        print('Choose option by entering a number for desired operation ')  #this is the menu section for menu options 
        print()
        for i in menu:
            print(i)
            
        x=input('Enter number for desired operation: ')
        
        if x=='1':
            y=SalariedEmployee()
            y.inputt()
            salaried_employees.append(y.storeEmployee())
            
        elif x=='2':
            z=WagedEmployee()
            z.inputt()
            waged_employees.append(z.storeEmployee())
            
        elif x=='3':
            print()
            print('Salaried Employees')
            for i in salaried_employees:
                print(i)
            print()
                
        elif x=='4':
            print()
            print('Waged Employees')
            for i in waged_employees:
                print(i)
            print()
                
        elif x=='5':
            print()
            print('Salaried Employees')
            for i in salaried_employees:
                print(i)
            print()
            print('Waged Employees')
            for i in waged_employees:
                print(i)
                
        elif x=='6':
            u=input('Enter name of employee you searching for: ')
            c=0
            t=0
            for j in employees[0]:
                    #print(employees[0][c][0]) this section just for debugging purposes
                if employees[0][c][0]==u:            #this checks for employee name in their profile with the desired employee  profile
                    for o in employees[0][c]:
                        print(o)
                c+=1
                        
            for i in employees[1]:
                #print(employees[1][t][0]) this section for debugging purposes
                if employees[1][t][0]==u:
                    for k in employees[1][t]:
                        print(k)
                t+=1
                    
        elif x=='7':
            break
                
main()