from Employee import Employee

class WagedEmployee(Employee): #this is the WagedEmployee class that has inherited the Employee class
    
    def __init__(self,n=None,a=None,ID=None,add=None,hr=0,hpw=0,wp=0,p='unknown'): #constructor method
        Employee.__init__(self,n,a,ID,add)
        self.hourly_rate=hr                                                        #this section is initializing variable objects
        self.hours_per_week=hpw
        self.weekly_pay=wp
        self.employee_personal=p
    
    def __str__(self):                             #string conversion method
        return(self.name+','+str(self.age)+','+str(self.identity_number)+','+self.employee_address+','+','+str(self.hourly_rate)+','+str(self.hours_per_week)+','+str(self.weekly_pay))
    
    def calculate_weekly_pay(self):                #method used to calculate weekly pay
        self.weekly_pay=int(self.hourly_rate)*int(self.hours_per_week)
        return str(self.weekly_pay)
        
    def inputt(self):                                #method to collect object information
        Employee.inputt(self) 
        self.hourly_rate=input('Enter hourly rate: ')
        self.hours_per_week=input('Enter hours per week: ')
        
    def display(self):
        Employee.display(self)
        print('Hourly rate: ',self.hourly_rate)
        print('Hours per week: ',self.hours_per_week)
        print('Weekly pay: ',self.weekly_pay)
        
        
    def storeEmployee(self):                                             #this is the method to store the data of the individual data
        p=(self.name,'Age: '+str(self.age),'Identity number: '+str(self.identity_number),'Address: '+self.employee_address,' Hourly rate: '+str(self.hourly_rate),'Hours per week: '+str(self.hours_per_week),'Weekly pay: '+str(self.weekly_pay))
        return p
    