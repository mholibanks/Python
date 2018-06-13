from sortsearch import *
from time import time
def main():
    lst=[]
    print('Enter list size of 2000,4000,6000 or 8000')
    size=int(input('Enter size of list: '))
    g=generate_number_list(size) #this function generates a list of integers
    for i in g: #this part adds the integers into list to be used by sorting methods
        lst.append(i)
    #print(lst) #debugging, seeing if each step does whats its supposed to
    print('1.Selection Sort') #these are the option the end-user has to execute
    print('2. Merge Sort')
    print('3.Bubble Sort')
    x=input('Enter type of sorting method: ')
    if x=='1':
        start_time=time()
        s=selection_sort(lst)
        end_time=time()
        time_taken=end_time-start_time
        print(time_taken)
    elif x=='2':
        start_time=time()
        m=merge_sort(lst)
        end_time=time()
        time_taken=end_time-start_time
        print(time_taken)        
    elif x=='3':
        start_time=time()
        b=bubble_sort(lst)
        end_time=time()    
        time_taken=end_time-start_time
        print(time_taken)        
main()