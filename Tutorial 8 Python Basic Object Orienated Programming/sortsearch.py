"""
Author: Gary Stewart
Description: Simple Python implementation of sorting and searching algorithms
Date: 27-09-2012
Log:
    fixed merge to iterative solution
"""

from random import *

def generate_number_list(size=1000): # generates list of random numbers
    lst = []
    for i in range(size):
        lst.append(randint(0,size-1))
    return lst

def selection_sort(lst):
    lst_len = len(lst)
    for bottom_index in range(lst_len - 1):
        min_index = bottom_index
        for i in range(bottom_index+1,lst_len): # find min_index
            if lst[i] < lst[min_index]:
                min_index = i
        lst[bottom_index],lst[min_index] = lst[min_index],lst[bottom_index] # swap
    return lst

def merge(lst1,lst2):  # for mergesort
    lst = []
    while len(lst1) > 0 and len(lst2) > 0:
        if lst1[0] < lst2[0]:
            lst.append(lst1[0])
            del lst1[0]
        else:
            lst.append(lst2[0])
            del lst2[0]
    return lst + lst1 + lst2

def merge_sort(lst):
    if len(lst) <= 1:
        return lst  
    else: 
        return merge(merge_sort(lst[0:len(lst)//2]),merge_sort(lst[len(lst)//2:]))
    
def bubble_sort(lst):
    swapped = True
    top = len(lst) - 1
    while top > 0 and swapped == True:
        i = 0
        swapped = False
        while i < top:
            if lst[i] > lst[i+1]:
                swapped = True
                lst[i],lst[i+1] = lst[i+1],lst[i] # swap
            i += 1
        top -= 1
    return lst

def linear_search(val,lst):
    index = 0
    found_index = None
    while index < len(lst) and found_index == None:
        if val == lst[index]:
            found_index = index
            break
        index += 1
    return found_index

def binary_search(val,lst,btm,top):
    mdl = btm+(top-btm)//2
    if lst == None or lst == [] or btm > top:
        return None  # val not found
    elif val == lst[mdl]:
        return mdl   # val found return position
    elif val < lst[mdl]:
        return binary_search(val,lst,btm,mdl-1) # search bottom half
    else:
        return binary_search(val,lst,mdl+1,top) # search top half
    
def main():
    print('Selection Sort')
    lst1 = generate_number_list(20)
    print(lst1)
    print(selection_sort(lst1))
    print('Merge Sort')
    lst2 = generate_number_list(20)
    print(lst2)
    print(merge_sort(lst2))
    print('Bubble Sort')
    lst3 = generate_number_list(20)
    print(lst3)
    print(bubble_sort(lst3))
    print('Linear Search')
    lst4 = generate_number_list(20)
    print(lst4)
    print(linear_search(10,lst4))
    print('Binary Search')
    lst5 = merge_sort(generate_number_list(20)) # list needs to be sorted for binary search
    print(lst5)
    print(binary_search(15,lst5,0,len(lst5)-1))
    
if __name__ == "__main__":
    main()
