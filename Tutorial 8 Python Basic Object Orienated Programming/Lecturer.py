class Lecturer:
    
    def __init__(self,n='unknown',staf_num=12345678):
        self.name=n
        self.staff_number=staf_num
        
    def __str__(self):
        s= str(self.name)+','+str(staff_number)
        return s
    
    def add_course(self,c='unknown'):
        self.courses.append(c)
    
    def input(self):
        self.name=input('Enter name: ')
        self.staff_number=input('Enter staff number: ') 
    
    def display(self):
        print('Name: ',self.name)
        print('Staff number: ',self.staff_number)
   
    def display_dictionary_values(self,d='unknown'):
        self.dictionary=d
        self.lst=[]
        for i in d:
            self.lst.append(i)
        return self.lst