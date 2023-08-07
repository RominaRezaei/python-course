############### ex 2 ses 5 *********************************
import math
def sec_deg_equation():
    while True:
           print ("lets start")
a = int(input ("zaribe a?"))
b = int(input("zaribe b?"))
c = int(input("zaribe c?"))
D = b**2 - (4*a*c)
if D<0:
        print ("this equation has no real roots")
elif D ==0:
        r = -b/(2*a)
        print("r1=r2=" , r )
else :
        r1 = (-b + math.sqrt(D)/ (2*a))
        r2 = (-b - math.sqrt(D)/ (2*a))
        print( "r1 , r2 respectively =" , r1 , r2 )

sec_deg_equation()
