def DecimalToIEEE754Single():
    print('Conversion to IEE754 Single Program Format')
    exp=-1
    exp1=0
    num=''
    sig=''
    b=''
    d=''
    f=''
    biased_expb=''
    n=input('Enter decimal number: ') #this is where you enter decimal number to be converted
    if n[0]=='-': 
        j='1'
    elif n[0]=='0' or str(int()):#this is to handle the sign bit of the IEEE754 number
        j='0'
    for i in n:
        if i=='-': continue
        num+=i
    x=num
    #this section is converstion of decimal number into IEEE754 single
    #print(x) #this is for debugging purposes checking whether input is desired
    number=x.split('.')  #split function to split the float number into integer and decimal point
    if len(number)==1:  #this is to eradicate the indexerror created when an integer number only is inserted so it prevents this by adding 00 to create a float and splits it into integer part and significand
        number.append('00')
    integer=number[0] #this is the part where integer is separeted from the significant number
    significand='.'+number[1]
    i=eval(integer)
    s=eval(significand)
    while True: #this part is responsible for conversion of integer into binary 
        r=str(i%2)
        b+=r
        i//=2
        if len(b)==8:
            break
    bn=b[::-1]
    #print(bn) this is used for debugging purposes ensure desired output is met
        
        
    while True: #this section is for conversion of decimal number into binary
        s*=2
        s=str(s)
        f=s.split('.')
        d+=f[0]
        ff='.'+f[1]
        s=float(ff)
        if len(d)==23:
            break
    dn='.'+d
    #print(dn) #this for debugging purposes, checking if desired output is met
    
    if bn=='00000000': #this section of code is for getting biased exponent for when decimal number has a integer = 0 e.g 0.65
        for i in dn:
            exp+=1
            if i=='1':break
        #print(exp)
        sig=dn[(exp+1):]
        #print(sig)
        
        biased_exponent=127-exp
        
        while True: #this section of code is converting biased exponent into binary
            r=str(biased_exponent%2)
            biased_expb+=r
            biased_exponent//=2
            if len(biased_expb)==8:break
        #print(biased_expb[::-1])
            
        print('['+str(j)+']'+'['+biased_expb[::-1]+']'+'['+sig+']')
            
        
    else:    #this section of code is for getting biased exponent when decimal num has an integer > 0 e.g 6.065
        for i in bn:
            exp1+=1
            if i=='1':break 
        #print(exp1)
        sig1=bn[exp1:]
        #print(sig1)
        exp2=len(sig1)
        #print(exp2)
        
        biased_exponent=127+exp2 #this is the biased exponent
        
        while True: #this section is for the conversion of biased exponent into binary digit
            r=str(biased_exponent%2)
            biased_expb+=r
            biased_exponent//=2
            if len(biased_expb)==8:break
        #print(biased_expb[::-1])
        
        print('['+str(j)+']'+'['+biased_expb[::-1]+']'+'['+sig1+dn[1:]+']')
        
DecimalToIEEE754Single()