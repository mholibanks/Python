#A program that calulates the area of circle
#Mholi Mncube
#8/03/2014

import math
import math
a=2
b=math.sqrt(2)
p,x=a,a
while p!=1:
  p=a/b
  b=math.sqrt(2+b)
  x*=p
        
print("Approximation of pi:",round(x,3))
radius=float(input("Enter the radius:\n"))
print("Area:",round(x*radius**2,3)) 