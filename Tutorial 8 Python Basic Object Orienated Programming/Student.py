class Student:
    
    def __init__(self, n='unknown', sn='unknown'):
        self.name = n
        self.student_number = sn
        self.courses = []
    
    def __str__(self):
        s = self.name + ',' + self.student_number
        for c in self.courses:
            s += '-' + str(c)
        return s
    
    def add_course(self, c):
        self.courses.append(c)
    
    def input(self):
        self.name = input('Enter name:')
        self.student_number = input('Enter student number:')

    def display(self):
        print('Name: ' + self.name)
        print('Student number: ' + self.student_number)