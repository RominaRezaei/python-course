#question 1
'''''
op= (input("enter op"))
num=int(input("num"))
if op = "factorial":
 if num < 0:
   print("error")
 elif num == 0:
   print("The factorial is 1")
 else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of is",factorial)
from math import sqrt
if op == "sqrt" :
  if num < 0 :
    result = "error"
else:
  result = sqrt(num)
print(result)
import math
if op == "sin":
    result = math.sin(math.radians(num))
       
if op == "cos":
      result = math.cos(math.radians(num))
      print(result)

if op == "tan":
     result = math.tan(math.radians(num))
     print(result)
if op == "cot":
         result = math.cot(math.radians(num))
         print(result)
break
'''
    #***************************************************************



    
    #question 2
''''
a=int(input("a"))
b=int(input("b"))
c=int(input("c"))
if a , b ,c >0:
 if(((a+b)<=c)or ((b+c)<=a)or ((c+a)<=b)):
    print("triangle")
 else:
    print ("not a triangle")
else:
  print("error")
  break
  '''
#********************************************************************


#question 3
name = input("enter your name:")
lastname = input ("enter your last name:")
g1 = input("enter the first grade")
g2 = input("enter the second grade")
g3 = input("enter the third grade")
avg= (g1 + g2 + g3)/3
if avg > 17:
 print("great")
if (avg<17) and (avg > 12):
 print("normal")
if avg < 12:
  print(failed)
