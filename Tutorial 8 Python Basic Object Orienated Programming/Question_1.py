from Lecturer import Lecturer #this is importing classes by names already created
from Course import Course
from Student import Student 

def main(): #main function
    courses={}
    lecturers={}
    students={}
    courses1=[]
    lecturers1=[]
    students1=[]
    print('University Member System:')
    print('1.Input Course')
    print('2.Input Lecturer')
    print('3.Input Student')
    print('4.Find Course')
    print('5.Find Lecturer')
    print('6.Find Student')
    print('7.Display Courses')
    print('8.Display Lecturers')
    print('9.Display Students')
    print('0.Quit')
    while True:
        x=input('Enter operation you wish to execute:')
        if x=='1':
            cc = input('Enter course code:')
            d = input('Enter description:')
            c=Course(cc,d)
            courses[cc]=d
        elif x=='2':
            n=input('Enter name of Lecturer: ' )
            staf_num=input('Enter staff number: ')
            l=Lecturer(n,staf_num)
            lecturers[staf_num]=n
        elif x=='3':
            n = input('Enter name:')
            sn = input('Enter student number:')                
            s=Student(n,sn)
            students[sn]=n
        elif x=='4':
            cc = input('Enter course code:')
            for i in courses:
                courses1.append(i)
                if i==cc:
                    print(courses[i])
        elif x=='5':
            staf_num=input('Enter staff number: ') 
            for i in lecturers:
                lecturers1.append(i)
                if i==staf_num:
                    print(lecturers[i])
        elif x=='6':
            sn=input('Enter student number:')
            for i in students:
                students1.append(i)
                if i==sn:
                    print(students[i])
        elif x=='7':
            l=Lecturer()
            print(l.display_dictionary_values(courses))
        elif x=='8':
            l=Lecturer()
            print(l.display_dictionary_values(lecturers))
        elif x=='9':
            l=Lecturer()            
            print(l.display_dictionary_values(students))
        elif x=='0':
            break
main()
    