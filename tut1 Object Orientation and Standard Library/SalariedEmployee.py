from Employee import Employee

class SalariedEmployee(Employee): #this is the salariedEmployee class that has inherited Employee class
    
    def __init__(self,n=None,a=None,ID=None,add=None,s=0,p='unknown'): #constructor method
        Employee.__init__(self,n,a,ID,add)                             #initializing objects
        self.salaray=s
        self.employee_personal=p                                       #this variable is for storing individual employee data that has been salaried
        
    def __str__(self):
        return(self.name+','+str(self.age)+','+str(self.identity_number)+','+self.employee_address+','+str(self.salary))
    
    
    def inputt(self):                                                  #this method is for input objects
        Employee.inputt(self)
        self.salary=input('Enter salary: ')
    
    def display(self):
        Employee.display(self)
        print('Salary: ',self.salary)
        
    def storeEmployee(self):                                           #this is the method to store the data of the individual data
        p=(self.name,'Age: '+str(self.age),'Identity number: '+str(self.identity_number),'Address: '+self.employee_address,'Salary: '+str(self.salary))
        return p
        