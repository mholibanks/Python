import functools
import operator
nums=[]
def main():
        x=input('Enter int numbers separated by space: ')
        num1=x.split(' ')
        for i in num1:
                nums.append(int(i))
        evens = filter(lambda x:x%2==0, nums)
        evens = map(lambda x: x, evens)
        multiplied = functools.reduce(operator.mul, evens)
        print(multiplied)
main()