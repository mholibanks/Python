def calculate_marks(a,b,c,d): # this function calculates the course average
    course_average=a+b+c+d
    return course_average

def excluded_or_not(a,b,c,d,):#this determines whether one has passed or excluded
    passed_or_failed=[] #empty list to insert marks greater than 50
    marks=[a,b,c,d] # list where marks are inserted and iterated through to check if >50
    for i in marks: #this oart checks for values passed if > 50 if they are added to passed or failed list
        if i>=50:
            passed_or_failed.append(i)
    if len(passed_or_failed)<3:
        print('You have been excluded')
    else:
        print('Passed')
def deansList(a,b,c,d): #this fuctions tells student if they made it into dean's list
    course_average=a+b+c+d
    if course_average/4>=70: #this happens if they get an overall pass of >70
        print('Congratulations, you have made it into the Dean\'s Merit list.')
    else:
        print()
def sciencebursary(a,b,c,d): #this function tells a student if they got bursary 
    course_ave=a+b+c+d
    if course_ave/4>=75:
        print('Congratulations, you have been awarded science faculty bursary.')
    else:
        print()
def main(): #this function calls all the function above also prompts user for arguments and passes them into functions
    name=input('Please enter your name: ')
    a=int(input('Enter course1 mark: '))
    b=int(input('Enter course2 mark: '))
    c=int(input('Enter course3 mark: '))
    d=int(input('Enter course4 mark: '))
    print('Dear',name.upper())
    excluded_or_not(a,b,c,d,)
    deansList(a,b,c,d)
    sciencebursary(a,b,c,d)
main()
            