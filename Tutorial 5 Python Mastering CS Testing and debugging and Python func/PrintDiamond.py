def triup(a,b): #this is the upper triangle to print half of the diamond
    j=b
    for i in range(a,b-1,2):
        j-=1
        print('{:^50}'.format(i*'$'))
#triup(1,10)
def tridown(b,a): #this is the lower inverted part of the diamond
    j=b
    for i in range(a,b,1):
        j-=2
        print('{:^50}'.format(j*'$'))
#tridown(11,1)
def main():
    b=int(input('Enter an even number >=4: '))
    a=1
    triup(a,b)
    tridown((b+1),a)
main()
#pass arguments that are greater than 6 for the program to show a diamon