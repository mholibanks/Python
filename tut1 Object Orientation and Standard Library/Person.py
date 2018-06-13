class Person: #this is the parent class or the fundemental
    
    def __init__(self,n='unknown',a=0): #contrustor method
        self.name = n                    #initializing objects
        self.age = a

    def increment_age(self):             #method used for increment of age
        self.age += 1
        
    def __str__(self):                    #string method to convert objects into strings
        return(self.name + ',' + str(self.age))

    def display(self):
        print('Name:',self.name)
        print('Age:',self.age)

