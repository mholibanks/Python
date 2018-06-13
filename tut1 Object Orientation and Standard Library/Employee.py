#23 Feb 2015 OOP
from Person import Person #importing class that will be used

class Employee(Person): #creating a class that inherits from another class

    def __init__(self,n=None,a=None,ID=0,add='unknown'): #contructor method
        Person.__init__(self,n,a)                        #intializing objects
        self.identity_number=ID
        self.employee_address=add
        
    def __str__(self):
        return(self.name+','+str(self.age)+','+str(self.identity_number)+','+self.employee_address)
    
    def inputt(self):                                    #method to input objects
            self.name=input('Enter name: ')
            self.age=input('Enter age: ')
            self.identity_number=input('Enter identity number: ')
            self.employee_address=input('Enter employee address: ')    
    
    def display(self):                                  #this method is yo display objects
        Person.display(self)
        print('Identity Number: ',self.identity_number)
        print('Employee\'s Adrress :',self.employee_address)
        

    

    