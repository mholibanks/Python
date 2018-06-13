def DecimalToBinary():
    print('Decimal To Binary Program')
    b='' #this is an empty string to store binary integer value in base 2
    d='' #this is an empty string to store binary decimal value in base 2
    ff='' #this is responsiple for string spliting of the float number
    decimal_points=[] #list of decimal point used to get binary decimal point value
    x=input('Enter number to be converted: ')
    number=x.split('.') #split function to split the float number into integer and decimal point
    if len(number)==1: #this is to eradicate the indexerror created when an integer number only is inserted so this is done by adding 00
        number.append('00')
    #this is the part where one splits the number into two parts integer part and signficand(decimal points or significant numbers)
    integer=number[0]  
    significand='.'+number[1]
    i=eval(integer)
    s=eval(significand)
    while i!=0: #this part is for conversion of the integer part into binary 
        r=str(i%2)
        b+=r
        i//=2
    print()
    while True: #this part is for the conversion of sigfinicand into binary
        s*=2
        s=str(s)
        f=s.split('.')
        d+=f[0]
        ff='.'+f[1]
        s=float(ff)
        if len(d)==8:
            break
        decimal_points.append(ff) 
    #print(decimal_points) this print statement is for debugging purposes to check desired results are the output
    print('Answer: '+x+' Base 10 equals '+str(b[::-1])+'.'+str(d)+' Base 2')

DecimalToBinary()