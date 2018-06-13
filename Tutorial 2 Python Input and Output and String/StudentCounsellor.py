#A program that interacts with the end-user
#Mholi Mncube
#1 May 2014

def student_counsellor(): 
    import time
    print("***Student Counsellor***")
    print()
    student_name=input("Greetings, I am a student counsellor, What is your prefered name of reference?: ")
    time.sleep(1)
    student_surname=input("That's a very interesting name, what is your surname?: ")
    time.sleep(1)
    print()
    year_of_birth=int(input("Aha! If I may ask what year were you born in?: "))
    time.sleep(2)
    print("Mmmh, if I count correctly you should be turning,",2014-int(year_of_birth),"years this year?") #rhetorical query
    time.sleep(1)
    favourite_course_code=input("So, what is your desired course code?: ")
    time.sleep(1)
    print("Well, you seem like an individual with a lot of potential.")
    time.sleep(1)
    print(student_name[:1]+"."+student_surname[:1]+",","tell me something...")# The student counsellor is thinking...
    time.sleep(0.5)
    course_code_description=input("Wait, what do the first 3 alphabets in course code stand for?: ")
    print("I meant these,",(favourite_course_code[:3]).upper())
    time.sleep(1)
    print()
    print((course_code_description).upper(),", oh that's a fantastic course!",sep='')
    time.sleep(1)
    year_completion_course=int(input("In what year, do you expect to finish your desired course?: "))
    time.sleep(2)
    print("Seemingly you will be,",(int(year_completion_course)-2014)+(2014-int(year_of_birth)),"years old when you graduate according to your plan. Good luck with your studies.",student_name) 
student_counsellor()
q=input("Press enter to exit.")
