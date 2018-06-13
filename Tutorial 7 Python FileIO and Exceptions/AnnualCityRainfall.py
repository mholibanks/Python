def enter_rainfall():
    months=['January','February','March','April','May','June','July','August','September','October','November','December']
    y=input('Enter <city_name>_<year>.dat in this format exactly: ') #this 
    f=open(y,'w')
    for i in months:
        print(i)
        x=input('Enter rainfall for twelve months: ')
        f.write(str(x)+'\n')
    f.close()
    
def read_rainfall():
    rainfall=[]
    valid_rainfall=[]
    invalid_rainfall=[]
    total_rain=0
    while len(rainfall)==0:    
        try:
            filename=input('Enter name of file for reading rainfall in format <city_name>_year: ')
            f=open(filename,'r')
        except ValueError as ve:
            print('This ValueError occured',ve)
        except TypeError as ve:
            print('This TypeError occured',ve)
        except FileNotFoundError as ve:
            print('This FileNotFoundError occured',ve)
        else:
            for i in f:
                rainfall.append(i)
                u=f.read()
                t=u.split()
                for j in t:
                    try:    #this section determines the invalid and valid rainfalls
                        type(j)                        
                        if type(eval(j))==float or type(eval(j))==int: #this part checks evaluates and checks type of rain value if it's valid adds it to 
                            valid_rainfall.append(j)
                            print(j)
                    except ValueError as ve:
                        print('Error')
                        invalid_rainfall.append(j)
                    except SyntaxError as ve:
                        print('Error')
                        invalid_rainfall.append(j)
                    except NameError as ve:
                        print('Error')
                        invalid_rainfall.append(j)  
                    else:
                        for k in valid_rainfall:
                            total_rain+=eval(k)
                        average_rainfall=total_rain/len(valid_rainfall)
                f=open('report.txt','a')
                f.write('The average rain fall is '+str(average_rainfall)+'\n'+'There were '+str(len(invalid_rainfall))+' invalid values'+'\n'+'There were '+str(len(valid_rainfall))+' valid values' )
                #print(valid_rainfall,invalid_rainfall)      #this line used to check sematics of above code              
            f.close()
            
def main():
    print('AnnualCityRainfall')
    while True:
        try:
            print('1.Enter Rainfall')
            print('2.Read Rainfall')
            print('3. Quit')
            x=int(input('Enter number (int) of the operation you would like to perform: '))
        except TypeError as ve:
            print('This TypeError occured',ve)
        except ValueError as ve:
            print('This ValueError occured',ve)
        else:
            if x==1:
                enter_rainfall()
            elif x==2:
                read_rainfall()
            elif x==3:
                print('Thank you for using AnnualCityRainfall, goodbye!')
                break
main()